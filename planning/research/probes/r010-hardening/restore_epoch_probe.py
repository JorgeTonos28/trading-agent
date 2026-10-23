"""Disposable logical restore fencing fixture; no OS/store or durability implementation."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
backup={'epoch':'BOOT1','generation':2,'attempt':'A2','receipts':[]}
ack_before_restore={'job':'J','epoch':'BOOT1','admitted':True,'received_at':45}
current_control_epoch='BOOT2'  # Trusted external control state, not restored from backup.
old_output={'epoch':'BOOT1','generation':2,'attempt':'A2'}
checks={'backup_generation_would_match':old_output['generation']==backup['generation'],
        'external_epoch_rejects_old_worker':old_output['epoch']!=current_control_epoch,
        'lost_ack_detected':ack_before_restore['admitted'] and not backup['receipts'],
        'gap_not_silently_recounted':True}
decision={'admission':'REJECTED_INCARNATION','recovery_status':'RECOVERY_GAP_UNKNOWN',
          'comparison_eligible':False,'new_financial_action':False,
          'note':'gap rule specified; no recovery of missing durable evidence actually demonstrated'}
out={'probe':'RESTORE_EPOCH_TOY','checks':checks,'passed':sum(checks.values()),'total':len(checks),
     'decision':decision,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'logical fixture, not real backup/worker fencing; fourth check is policy assignment, not enforcement'}
(HERE/'restore-epoch-result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'passed':out['passed'],'total':out['total'],'scope':out['scope']}))
