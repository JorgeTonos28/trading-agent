from pathlib import Path
from decimal import Decimal
import sys,hashlib,json,platform,socket
here=Path(__file__).resolve().parent;root=here.parents[3]
out=here/'result-01.json'
if out.exists():raise RuntimeError('NEW_ATTEMPT_REQUIRED')
def deny(*a,**k):raise RuntimeError('NO_NETWORK_IN_PYTHON_PROBE')
socket.socket=deny;socket.create_connection=deny
sys.path[:0]=[str(root/'.local/r009-nautilus-deps'),str(root/'.local/r020-eval-deps')]
rows=[]
def record(k,status,detail):rows.append({'id':k,'status':status,'detail':detail})
wheel=root/'.local/r009-wheel/nautilus_trader-1.231.0-cp314-cp314-win_amd64.whl'
got=hashlib.sha256(wheel.read_bytes()).hexdigest();record('ARTIFACT_HASH','PASS' if got=='295b67b127f67429ebb9d937bd11448f930bee697fca6a8e0ec1de343ad3c68c' else 'FAIL',got)
try:
 import nautilus_trader
 record('CORE_IMPORT_VERSION','PASS' if nautilus_trader.__version__=='1.231.0' else 'FAIL',nautilus_trader.__version__)
 from nautilus_trader.model.instruments import Equity
 from nautilus_trader.model.identifiers import InstrumentId,Symbol
 from nautilus_trader.model.objects import Price,Quantity
 from nautilus_trader.model.currencies import USD
 eq=Equity(instrument_id=InstrumentId.from_str('FIXTURE.SIM'),raw_symbol=Symbol('FIXTURE'),currency=USD,price_precision=2,price_increment=Price.from_str('0.01'),lot_size=Quantity.from_int(1),ts_event=0,ts_init=0)
 record('SYNTHETIC_EQUITY','PASS' if eq.size_precision==0 and str(eq.price_increment)=='0.01' else 'FAIL',{'size_precision':eq.size_precision,'price_increment':str(eq.price_increment)})
 try:
  q=eq.make_qty(Decimal('0.5'));record('FRACTIONAL_MODEL_BEHAVIOR','PASS' if q.as_double()==0 else 'FAIL',{'requested':'0.5','represented':str(q),'fractional_supported':False})
 except (ValueError,TypeError) as e:record('FRACTIONAL_MODEL_BEHAVIOR','PASS',{'rejected':type(e).__name__,'fractional_supported':False})
except Exception as e:record('CORE_COMPONENTS','ERROR',{'type':type(e).__name__,'missing_module':getattr(e,'name',None)})
try:
 from nautilus_trader.backtest.engine import BacktestEngine
 record('BACKTEST_ENGINE_IMPORT','PASS','IMPORTED_ONLY_NOT_INSTANTIATED_OR_RUN')
except Exception as e:record('BACKTEST_ENGINE_IMPORT','ERROR',{'type':type(e).__name__,'missing_module':getattr(e,'name',None)})
result={'observed_on':'2026-10-15','attempt':'QE0-01','python':platform.python_version(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'wheel_sha256':got,'rows':rows,'counts':{k:sum(r['status']==k for r in rows) for k in ['PASS','FAIL','ERROR']},'scope':'ARTIFACT_AND_COMPONENT_ONLY','engine_selected':False,'backtest_executed':False,'QP1_10_accepted':False,'history_accessed':False,'strategy_trials':0,'target_acceptance':'TARGET_ACCEPTANCE_DEFERRED','implementation_locked':True,'incremental_spend':0}
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result['counts']));raise SystemExit(0)
