from pathlib import Path
from decimal import Decimal as D
import sys,socket,json,hashlib
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'rounding-result-01.json'
if out.exists():raise RuntimeError('KEEP_ATTEMPT_NEW_ID_REQUIRED')
def deny(*a,**k):raise RuntimeError('NO_PYTHON_NETWORK')
socket.socket.connect=deny;socket.socket.connect_ex=deny;socket.create_connection=deny
sys.path[:0]=[str(root/'.local/r009-nautilus-deps'),str(root/'.local/r020-eval-deps')]
from nautilus_trader.model.instruments import Equity
from nautilus_trader.model.identifiers import InstrumentId,Symbol
from nautilus_trader.model.objects import Price,Quantity
from nautilus_trader.model.currencies import USD
eq=Equity(instrument_id=InstrumentId.from_str('FIXTURE.SIM'),raw_symbol=Symbol('FIXTURE'),currency=USD,price_precision=2,price_increment=Price.from_str('0.01'),lot_size=Quantity.from_int(1),ts_event=0,ts_init=0)
rows=[]
for v,expected_default,expected_floor in [('1.6',2,1),('1.5',2,1),('2.5',2,2),('12.999',13,12)]:
 a=eq.make_qty(D(v)).as_double();b=eq.make_qty(D(v),round_down=True).as_double()
 rows.append({'value':v,'default':a,'floor':b,'pass':a==expected_default and b==expected_floor and D(str(b))<=D(v)})
try:eq.make_qty(D('.5'),round_down=True);small=False
except ValueError:small=True
rows.append({'value':'.5','round_down_rejects_zero':small,'pass':small})
z={'observed_on':'2026-10-15','attempt':'QE1-ROUND-01','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,'pass_count':sum(x['pass'] for x in rows),'total':len(rows),'scope':'QUANTITY_COMPONENT_NOT_RISK_OR_EXECUTION_ADAPTER','default_can_exceed_input':rows[0]['default']>float(rows[0]['value']),'Risk_accepted':False,'QP6_accepted':False,'history_accessed':False,'strategy_trials':0,'backtest_executed':False,'implementation_locked':True,'target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
out.write_text(json.dumps(z,indent=2)+'\n',encoding='utf-8');print(json.dumps({'pass':z['pass_count'],'total':z['total'],'QP6_accepted':False}));raise SystemExit(0 if all(x['pass'] for x in rows) else 1)
