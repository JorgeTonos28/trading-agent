"""Disposable algebraic counterexamples; no market data or trading interfaces."""
from decimal import Decimal as D
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

output_path=Path(__file__).parent/'result-next.json'
if output_path.exists():
    raise FileExistsError('Future result already exists; preserve evidence and use a new preregistered attempt')
rows=[]
def observe(name,values,expected):
    rendered={key:str(value) for key,value in values.items()}
    rows.append({'id':name,'observed':rendered,'expected':expected,
                 'status':'PASS' if rendered==expected else 'FAIL'})

q=D('10')
observe('GAIN_MARK_VS_ENTRY',{'entry':q*max(D('100')-D('110'),D(0)),
 'remaining':q*(D('120')-D('110'))},{'entry':'0','remaining':'100'})
observe('LOSS_ALREADY_IN_EQUITY',{'entry':q*(D('100')-D('80')),
 'remaining':q*(D('90')-D('80'))},{'entry':'200','remaining':'100'})
observe('PENDING_SALE_NOT_CASH',{'confirmed_free_cash':D('25'),
 'cash_after_unconfirmed_sale':D('25')},{'confirmed_free_cash':'25','cash_after_unconfirmed_sale':'25'})
observe('EXCLUSIVE_COVERAGE',{'correct':(D('4')+D('6'))*D('10'),
 'double_counted':(D('4')+D('6')+D('6'))*D('10')},{'correct':'100','double_counted':'160'})
observe('MOST_RESTRICTIVE',{'quantity':min(map(D,['100','8','5','7','6','4']))},{'quantity':'4'})
affordable=[n for n in range(6) if D(n)*D('10')+D('2')<=D('35')]
observe('FIXED_FEE',{'quantity':max(affordable)},{'quantity':'3'})
feasible=[n for n in range(0,51,10) if D(n)*D('3')<=D('100')]
observe('LOT_ROUND_DOWN',{'quantity':max(feasible)},{'quantity':'30'})
required_bounds=[D('9'),None,D('7')]
observe('UNKNOWN_REQUIRED',{'positive_quantity_admissible':all(x is not None for x in required_bounds)},
 {'positive_quantity_admissible':'False'})
result={'scope':'SYNTHETIC_ALGEBRA_NOT_RISK_ENGINE_OR_BACKTEST','preregistered_on':'2026-10-13',
 'captured_utc':datetime.now(timezone.utc).isoformat(),
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'network_calls':0,'financial_interfaces':0,'policies_approved':False,
 'rows':rows,'pass':sum(r['status']=='PASS' for r in rows),'total':len(rows)}
with output_path.open('x',encoding='utf-8') as output:
    output.write(json.dumps(result,indent=2)+'\n')
print(json.dumps({'pass':result['pass'],'total':result['total'],'scope':result['scope']}))
