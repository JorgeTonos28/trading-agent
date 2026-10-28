from datetime import datetime, timezone
from pathlib import Path
import hashlib,json,sqlite3
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'restore-01.json'
if out.exists():raise FileExistsError('Preserve attempt')
work=root/'.local/h9-demand-ledger'
anchor=json.loads((work/'outside-backup-anchor.json').read_text(encoding='utf-8'))
c=sqlite3.connect('file:'+str((work/'restored.db').resolve()).replace('\\','/')+'?mode=ro',uri=True)
row=c.execute('SELECT state,generation,attempt FROM jobs WHERE id=?',(anchor['job'],)).fetchone()
receipt=c.execute('SELECT bodyhash FROM receipts WHERE job=?',(anchor['job'],)).fetchone();c.close()
rows=[]
def case(id,observed,expected):rows.append({'id':id,'observed':observed,'expected':expected,'status':'PASS' if observed==expected else 'FAIL'})
case('ACTUAL_RESTORED_JOB_STATE',list(row),['RUNNING',1,'a1'])
case('ACTUAL_RESTORED_RECEIPT_ABSENT',receipt is None,True)
new_epoch=2;old_envelope_epoch=anchor['epoch']
case('ACTUAL_RESTORED_OLD_ENVELOPE_FENCED',old_envelope_epoch==new_epoch,False)
def recovery_verdict(history_known,ack_seen,sealed_body_verified):
    if not history_known:return 'UNKNOWN_HISTORY_BLOCK_ATTEMPTS_AND_ADMISSION'
    if ack_seen and not sealed_body_verified:return 'RECOVERY_GAP_BLOCK_ATTEMPTS_AND_ADMISSION'
    if ack_seen:return 'RECONSTRUCT_ORIGINAL_RECEIPT_ONLY_NO_NEW_WINNER'
    return 'NORMAL_ADMISSION_REQUIRES_OTHER_GATES'
case('HASH_ONLY_ACK_NOT_RECOVERY',recovery_verdict(True,bool(anchor['acknowledged_bodyhash']),False),'RECOVERY_GAP_BLOCK_ATTEMPTS_AND_ADMISSION')
case('NO_ANCHORS_NOT_ASSUME_UNSEEN',recovery_verdict(False,False,False),'UNKNOWN_HISTORY_BLOCK_ATTEMPTS_AND_ADMISSION')
case('FULL_VERIFIED_HISTORY_RECONSTRUCTS_OLD_IDENTITY',recovery_verdict(True,True,True),'RECONSTRUCT_ORIGINAL_RECEIPT_ONLY_NO_NEW_WINNER')
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'READ_ACTUAL_RESTORED_FIXTURE_AND_RECOVERY_GATE_NOT_OPERATIONAL_RESTORE',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,
 'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},
 'restored_db_read_only':True,'anchor_security_or_auth_proven':False,'PostgreSQL_or_Financial_Core_accepted':False,
 'implementation_locked':True,'holdout':'INTEGRITY_UNKNOWN','target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'failed':[r for r in rows if r['status']!='PASS']}))
