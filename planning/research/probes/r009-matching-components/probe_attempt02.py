"""Disposable native matcher experiment. No strategy, financial service or network calls."""
from pathlib import Path
from decimal import Decimal
from datetime import datetime, timezone
import hashlib, json, os, platform, socket, sys, zipfile

here=Path(__file__).resolve().parent
root=here.parents[3]
attempt=sys.argv[1] if len(sys.argv)>1 else '01'
out=here/f'result-{attempt}.json'
if out.exists(): raise FileExistsError('Preserve prior capture; new attempt required')
def deny(*a,**k): raise RuntimeError('No Python network in component probe')
socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny
sys.path[:0]=[str(root/'.local/r009-nautilus-deps'),str(root/'.local/r020-eval-deps')]
wheel=root/'.local/r009-wheel/nautilus_trader-1.231.0-cp314-cp314-win_amd64.whl'
wheel_hash=hashlib.sha256(wheel.read_bytes()).hexdigest()
assert wheel_hash=='295b67b127f67429ebb9d937bd11448f930bee697fca6a8e0ec1de343ad3c68c'
from nautilus_trader.backtest.engine import OrderMatchingEngine
from nautilus_trader.backtest.models import FillModel, MakerTakerFeeModel
from nautilus_trader.cache.cache import Cache
from nautilus_trader.common.component import TestClock, MessageBus
from nautilus_trader.common.factories import OrderFactory
from nautilus_trader.model.enums import AccountType, BookType, OmsType, OrderSide
from nautilus_trader.model.identifiers import InstrumentId, Symbol, TraderId, StrategyId, AccountId
from nautilus_trader.model.objects import Price, Quantity
from nautilus_trader.model.instruments import Equity
from nautilus_trader.model.currencies import USD
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.position import Position
from nautilus_trader.model.events import OrderSubmitted
from nautilus_trader.core.uuid import UUID4

rows=[]
traces={}
def check(name, observed, expected):
    rows.append(dict(id=name,observed=observed,expected=expected,status='PASS' if observed==expected else 'FAIL'))

class Lab:
    def __init__(self, consume=False):
        self.clock=TestClock(); self.clock.set_time(1)
        self.trader=TraderId('FIXTURE-001'); self.account=AccountId('SIM-001')
        self.bus=MessageBus(trader_id=self.trader,clock=self.clock)
        self.cache=Cache(database=None)
        self.eq=Equity(instrument_id=InstrumentId.from_str('FICTION.SIM'),raw_symbol=Symbol('FICTION'),currency=USD,price_precision=2,price_increment=Price.from_str('0.01'),lot_size=Quantity.from_int(1),ts_event=0,ts_init=0)
        self.cache.add_instrument(self.eq)
        self.events=[]; self.position_id=None
        self.bus.register(endpoint='ExecEngine.process',handler=self.receive)
        self.matcher=OrderMatchingEngine(instrument=self.eq,raw_id=1,fill_model=FillModel(),fee_model=MakerTakerFeeModel(),book_type=BookType.L1_MBP,oms_type=OmsType.HEDGING,account_type=AccountType.CASH,msgbus=self.bus,cache=self.cache,clock=self.clock,liquidity_consumption=consume)
        self.factory=OrderFactory(trader_id=self.trader,strategy_id=StrategyId('LAB-001'),clock=self.clock)
    def receive(self,event):
        order=self.cache.order(event.client_order_id)
        order.apply(event)
        self.cache.update_order(order)
        row={'type':type(event).__name__,'order':str(event.client_order_id)}
        if type(event).__name__=='OrderFilled':
            row.update(price=str(event.last_px),qty=str(event.last_qty))
            if event.position_id is not None:
                pos=self.cache.position(event.position_id)
                if pos is None:
                    pos=Position(self.eq,event)
                    self.cache.add_position(pos,OmsType.HEDGING)
                else:
                    pos.apply(event); self.cache.update_position(pos)
                self.position_id=pos.id
        self.events.append(row)
    def quote(self,bid,ask=None,size=100):
        self.clock.set_time(self.clock.timestamp_ns()+1)
        ns=self.clock.timestamp_ns()
        self.matcher.process_quote_tick(QuoteTick(instrument_id=self.eq.id,bid_price=Price.from_str(f'{bid:.2f}'),ask_price=Price.from_str(f'{(bid if ask is None else ask):.2f}'),bid_size=Quantity.from_int(size),ask_size=Quantity.from_int(size),ts_event=ns,ts_init=ns))
    def submit(self,order,position_id=None):
        self.cache.add_order(order,position_id=position_id)
        order.apply(OrderSubmitted(trader_id=order.trader_id,strategy_id=order.strategy_id,instrument_id=order.instrument_id,client_order_id=order.client_order_id,account_id=self.account,event_id=UUID4(),ts_event=self.clock.timestamp_ns(),ts_init=self.clock.timestamp_ns()))
        self.cache.update_order(order)
        self.matcher.process_order(order,self.account)
        return order
    def buy(self,qty):
        return self.submit(self.factory.market(self.eq.id,OrderSide.BUY,Quantity.from_int(qty)))
    def protect(self,limit=False):
        if limit:
            order=self.factory.stop_limit(self.eq.id,OrderSide.SELL,Quantity.from_int(2),Price.from_str('94.00'),Price.from_str('95.00'))
        else:
            order=self.factory.stop_market(self.eq.id,OrderSide.SELL,Quantity.from_int(2),Price.from_str('95.00'))
        return self.submit(order,self.position_id)
    def fills(self,order):
        return [e for e in self.events if e['type']=='OrderFilled' and e['order']==str(order.client_order_id)]

def scenario(name,fn):
    try: fn()
    except Exception as exc:
        rows.append(dict(id=name,status='ERROR',error_type=type(exc).__name__,error=str(exc)[:500]))

def gap_market():
    x=Lab();x.quote(100);x.buy(10);o=x.protect();x.quote(90)
    fills=x.fills(o);check('GAP_MARKET_PRICE',[e['price'] for e in fills],['90.00'])
    check('GAP_MARKET_QTY',[e['qty'] for e in fills],['2']);traces['gap_market']=x.events
def gap_limit():
    x=Lab();x.quote(100);x.buy(10);o=x.protect(True);x.quote(90)
    check('GAP_LIMIT_NOT_FILLED',len(x.fills(o)),0)
    x.quote(96);f=x.fills(o)
    check('GAP_LIMIT_RECOVERY_FILLED',len(f),1)
    check('GAP_LIMIT_PRICE_BOUND',all(Decimal(e['price'])>=Decimal(94) for e in f),True)
    traces['gap_limit']=x.events
def paths():
    counts=[]
    for label,path in [('O_H_L_C',[100,102,90,92]),('O_L_H_C',[100,90,102,92])]:
        x=Lab();x.quote(100);x.buy(10);o=x.protect(True)
        for bid in path: x.quote(bid)
        counts.append(len(x.fills(o)));traces[label]=x.events
    check('SAME_OHLC_DIFFERENT_EXECUTION',counts,[0,1])
def liquidity(consume):
    x=Lab(consume);x.quote(100,size=5);o1=x.buy(3);o2=x.buy(3)
    total=sum(Decimal(e['qty']) for o in [o1,o2] for e in x.fills(o))
    check('L1_CONSUMPTION_'+str(consume),str(total),'5' if consume else '6')
    traces['liquidity_'+str(consume)]=x.events
scenario('GAP_MARKET',gap_market);scenario('GAP_LIMIT',gap_limit);scenario('PATHS',paths)
scenario('LIQUIDITY_FALSE',lambda:liquidity(False));scenario('LIQUIDITY_TRUE',lambda:liquidity(True))
result=dict(captured_utc=datetime.now(timezone.utc).isoformat(),attempt=attempt,python=platform.python_version(),scope='NATIVE_MATCHING_COMPONENT_FICTITIOUS_QUOTES_ONLY_NO_STRATEGY',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),wheel_sha256=wheel_hash,rows=rows,traces=traces,counts={k:sum(r['status']==k for r in rows) for k in ['PASS','FAIL','ERROR']},strategy_trials=0,historical_backtests=0,market_data_accessed=False,QP1_10_accepted=False,broker_selected=False,engine_selected=False,implementation_locked=True,target_acceptance='TARGET_ACCEPTANCE_DEFERRED')
with out.open('x',encoding='utf-8') as f: json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result['counts']))
