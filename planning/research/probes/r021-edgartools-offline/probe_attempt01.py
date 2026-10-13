"""Disposable synthetic XML/library probe; no network or financial data."""
import builtins
import hashlib
import importlib.metadata
import json
from pathlib import Path
import sys

output=Path(__file__).parent/'result-01.json'
if output.exists():raise FileExistsError('Preserve prior attempt; do not overwrite')
sys.path.insert(0,sys.argv[1])
blocked=[]
def audit(event,args):
    if event in {'socket.connect','socket.getaddrinfo','socket.gethostbyname','socket.gethostbyaddr'}:
        blocked.append(event)
        raise RuntimeError('NETWORK_DISABLED_IN_PROBE')
sys.addaudithook(audit)
def no_input(*args,**kwargs):
    blocked.append('input')
    raise RuntimeError('USER_INPUT_DISABLED_IN_PROBE')
builtins.input=no_input

def fixture(code='P',footnote='Purchase on an exchange.',price=True,form='4',derivative=False,owners=1):
    owner=''.join(f'''<reportingOwner><reportingOwnerId><rptOwnerCik>{9999900000+i}</rptOwnerCik><rptOwnerName>FICTITIOUS OWNER {i}</rptOwnerName></reportingOwnerId><reportingOwnerRelationship><isDirector>1</isDirector><isOfficer>0</isOfficer><isTenPercentOwner>0</isTenPercentOwner><isOther>0</isOther></reportingOwnerRelationship></reportingOwner>''' for i in range(owners))
    tag='derivative' if derivative else 'nonDerivative'
    price_xml='<transactionPricePerShare><value>100</value></transactionPricePerShare>' if price else ''
    extra='''<conversionOrExercisePrice><value>10</value></conversionOrExercisePrice><underlyingSecurity><underlyingSecurityTitle><value>FICTITIOUS Common</value></underlyingSecurityTitle><underlyingSecurityShares><value>10</value></underlyingSecurityShares></underlyingSecurity>''' if derivative else ''
    return f'''<ownershipDocument><schemaVersion>X0306</schemaVersion><documentType>{form}</documentType><periodOfReport>2020-01-02</periodOfReport><issuer><issuerCik>9999999999</issuerCik><issuerName>FICTITIOUS ISSUER</issuerName><issuerTradingSymbol>FAKE</issuerTradingSymbol></issuer>{owner}<{tag}Table><{tag}Transaction><securityTitle><value>FICTITIOUS Common</value></securityTitle><transactionDate><value>2020-01-02</value></transactionDate><transactionCoding><transactionFormType>4</transactionFormType><transactionCode>{code}</transactionCode><equitySwapInvolved>0</equitySwapInvolved></transactionCoding><transactionAmounts><transactionShares><value>10</value></transactionShares>{price_xml}<transactionAcquiredDisposedCode><value>A</value></transactionAcquiredDisposedCode></transactionAmounts>{extra}<postTransactionAmounts><sharesOwnedFollowingTransaction><value>20</value></sharesOwnedFollowingTransaction></postTransactionAmounts><ownershipNature><directOrIndirectOwnership><value>D</value></directOrIndirectOwnership></ownershipNature><footnoteId id="F1"/></{tag}Transaction></{tag}Table><footnotes><footnote id="F1">{footnote}</footnote></footnotes><ownerSignature><signatureName>FICTITIOUS OWNER</signatureName><signatureDate>2020-01-03</signatureDate></ownerSignature></ownershipDocument>'''

result={'scope':'SYNTHETIC_OFFLINE_DATA_LIBRARY_NOT_BACKTEST','observed_on':'2026-10-13',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'provider_selected':False,'PIT_proven':False,'fixtures':[],'network_guard':'PYTHON_AUDIT_NOT_OS_ISOLATION'}
try:
    import pandas as pd
    from edgar.xmltools import parse_xml,find_element
    from edgar.ownership.models import Footnotes
    from edgar.ownership.table_containers import NonDerivativeTable,DerivativeTable
    from edgar.ownership.forms import Ownership
    result['edgartools_version']=importlib.metadata.version('edgartools')
    case_definitions=[('P_EXCHANGE',{}),('P_PRIVATE',{'footnote':'Private purchase from another person; not executed on an exchange.'}),
      ('F_TAX',{'code':'F','footnote':'Shares withheld for tax.'}),
      ('M_DERIVATIVE',{'code':'M','derivative':True,'footnote':'Exercise of a derivative.'}),
      ('PRICE_MISSING',{'price':False}),('AMENDMENT',{'form':'4/A'}),('JOINT_OWNERS',{'owners':2})]
    for name,options in case_definitions:
        xml=fixture(**options)
        row={'id':name,'fixture_sha256':hashlib.sha256(xml.encode()).hexdigest(),'mode':'STRUCTURAL_TABLE_ONLY',
             'full_owner_enrichment_tested':False}
        try:
            root=parse_xml(xml)
            derivative=options.get('derivative',False)
            table_tag=find_element(root,'derivativeTable' if derivative else 'nonDerivativeTable')
            table=(DerivativeTable if derivative else NonDerivativeTable).extract(table_tag,form=options.get('form','4'))
            data=table.transactions.data
            values=data.iloc[0]
            parsed_price=None if pd.isna(values['Price']) else str(values['Price'])
            row.update(code=str(values['Code']),shares=str(values['Shares']),price=parsed_price,
                footnote_id_preserved='F1' in str(values.get('footnotes','')),
                form=table.form,transaction_rows=len(data),
                market_rows=None if derivative else len(table.market_trades),
                raw_owner_count=xml.count('<reportingOwner>'),
                expected_owner_count=options.get('owners',1))
            row['checks']={
                'code_preserved':row['code']==options.get('code','P'),
                'quantity_preserved':float(values['Shares'])==10,
                'footnote_ref_preserved':row['footnote_id_preserved'],
                'price_missing_preserved':row['price'] is None if not options.get('price',True) else float(values['Price'])==100,
                'form_preserved':row['form']==options.get('form','4'),
                'one_economic_row':row['transaction_rows']==1}
            row['status']='PASS_STRUCTURAL' if all(row['checks'].values()) else 'FAIL_STRUCTURAL'
            if name=='P_PRIVATE':row['semantic_limit']='P_PRIVATE_INCLUDED_IN_MARKET_TRADES' if row['market_rows']==1 else 'OBSERVE_DIFFERENT_CLASSIFICATION'
            if name=='JOINT_OWNERS':row['semantic_limit']='RAW_OWNERS_2_TABLE_ROW_1_OWNER_ENRICHMENT_NOT_TESTED'
        except Exception as error:
            row.update(status='ERROR_STRUCTURAL',error_class=type(error).__name__)
        result['fixtures'].append(row)
    try:
        Ownership.from_xml(fixture())
        result['full_factory']={'status':'COMPLETED','network_or_input_attempt_observed':False}
    except Exception as error:
        result['full_factory']={'status':'BLOCKED_OR_ERROR','error_class':type(error).__name__,
          'semantic_limit':'FULL_FACTORY_NOT_PROVEN_OFFLINE_NO_ENRICHMENT_STUB_ADDED'}
except Exception as error:
    result['import_error_class']=type(error).__name__
result['blocked_events']=blocked
result['structural_pass']=sum(r.get('status')=='PASS_STRUCTURAL' for r in result['fixtures'])
result['structural_total']=len(result['fixtures'])
with output.open('x',encoding='utf-8') as report:report.write(json.dumps(result,indent=2)+'\n')
print(json.dumps({'structural_pass':result['structural_pass'],'total':result['structural_total'],'full_factory':result.get('full_factory'),'import_error':result.get('import_error_class')}))
