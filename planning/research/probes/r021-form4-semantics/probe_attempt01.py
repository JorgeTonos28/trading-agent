"""Public data-library components on fictional XML; no SEC access or enrichment."""
from pathlib import Path
import hashlib,json,sys
out=Path(__file__).with_name('result-01.json')
if out.exists():raise FileExistsError('Do not overwrite evidence')
sys.path.insert(0,sys.argv[1]);blocked=[]
def audit(event,args):
 if event in {'socket.connect','socket.getaddrinfo','socket.gethostbyname'}:
  blocked.append(event);raise RuntimeError('NETWORK_DISABLED_IN_PROBE')
sys.addaudithook(audit)
r={'observed_on':'2026-10-14','scope':'SYNTHETIC_COMPONENTS_NOT_DATASET_ADMISSION',
   'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':[],'observations':{}}
def check(id,yes):r['checks'].append({'id':id,'status':'PASS' if yes else 'FAIL'})
try:
 from edgar.ownership.models import Footnotes
 from edgar.ownership.forms import _parse_aff10b5_one
 from edgar.xmltools import parse_xml
 for raw,expected,label in [(None,None,'MISSING'),('1',True,'ONE'),('0',False,'ZERO'),('true',True,'TRUE'),('false',False,'FALSE'),(' TRUE ',True,'TRIM_CASE'),('',None,'EMPTY'),('yes',None,'INVALID'),('unknown',None,'UNKNOWN')]:
  check('FLAG_'+label,_parse_aff10b5_one(raw)==expected)
 markup='<ownershipDocument><footnotes><footnote id="F1">FICTITIOUS private <b>purchase</b> with extra text.</footnote></footnotes></ownershipDocument>'
 notes=Footnotes.extract(parse_xml(markup))
 check('FULL_MARKUP_TEXT_PRESERVED',all(word in notes.get('F1','') for word in ['FICTITIOUS','private','purchase','extra text']))
 check('MISSING_REF_NULL',notes.get('F999') is None)
 empty=Footnotes.extract(parse_xml('<ownershipDocument/>'))
 check('NO_NOTES_EMPTY_NOT_EVIDENCE',len(empty)==0)
 duplicate=Footnotes.extract(parse_xml('<ownershipDocument><footnotes><footnote id="F1">FICTITIOUS first</footnote><footnote id="F1">FICTITIOUS second</footnote></footnotes></ownershipDocument>'))
 r['observations']['duplicate_id_behavior']={'count_after_extract':len(duplicate),'retained_text':duplicate.get('F1')}
 check('DUPLICATE_COLLAPSE_OBSERVED',len(duplicate)==1)
 r['observations']['missing_invalid_collapsed_to_None']=_parse_aff10b5_one(None) is _parse_aff10b5_one('yes')
 r['row_plan_status']='UNKNOWN_COMPONENT_PROBE_NOT_ROW_ADJUDICATION'
 r['library_pin']='edgartools5.62.0';r['full_factory_executed']=False
except Exception as e:r['library_error_class']=type(e).__name__
r.update(blocked_network_events=blocked,pass_count=sum(c['status']=='PASS' for c in r['checks']),total=len(r['checks']),PIT_proven=False)
with out.open('x',encoding='utf-8') as f:f.write(json.dumps(r,indent=2)+'\n')
print(json.dumps({'pass_count':r['pass_count'],'total':r['total'],'library_error':r.get('library_error_class'),'duplicate':r['observations'].get('duplicate_id_behavior')}))
