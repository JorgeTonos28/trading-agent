# ADR-024 — APScheduler acotado + PostgreSQL para PAPER

- Registro y aprobación: 2026-10-29, instrucción explícita del propietario.
- Estado: **DECIDED — CONDITIONAL_DESIGN_DIRECTION_ONLY**; Q-063/A.
- D-025/D-026: dirección aprobada; especificación/configuración/suficiencia continúan RESEARCHING.
- Antecedente: [propuesta Q-063](../research/D-025_026_PAPER_workflow_storage_decision_RC0.md), checkpoint 5eed577.

## Dirección y responsabilidades

APScheduler 3.x se reutiliza únicamente para calendario y wakeups, con un único scheduler propietario; no compartir job stores entre procesos. PostgreSQL conserva durablemente jobs, attempts, manifests, deadlines, outbox, receipts, leases, epochs y estados de reconstrucción. Reconstruir wakeups desde reglas y estados persistidos: una notificación perdida no pierde un job ni elimina su deadline. Versiones y dependencias compatibles se fijarán mediante evidencia antes del freeze.

El supervisor/control confiable conserva admisión y recuperación; Financial Core conserva decisiones financieras, reservas y ejecución. APScheduler no es autoridad financiera, de admisión, recovery u órdenes. Ningún callable, import, SQL o tarea serializada procede del modelo. Un fallo no crea autoridad alternativa ni permite suponer protección confirmada o reanudar un incidente material.

Roles, credenciales, permisos y stores financieros/control se separan efectivamente. Compartir servidor PostgreSQL no demuestra aislamiento. Agentes sin acceso SQL ni secretos financieros. Validar frontera, procedimientos y permisos; no sustituirlos por nombres de DB.

## Durabilidad, recuperación y límites

Especificar y verificar crash antes/después de commit, dispatch, ack y receipt; duplicados, timeouts, leases obsoletos, pérdida de conectividad, restart y restore. At-least-once no significa exactly-once. No reenviar órdenes financieras a ciegas; reconciliar IDs/estado broker y ledger. Epoch nuevo no repara evidencia histórica perdida.

Definir WAL, commit, fsync, backup/restore, RPO/RTO, fallo de disco/escritura y reglas fail-closed. SQLite o fixtures no acreditan PostgreSQL/hardware. Configuración y envelope/suficiencia numéricos son P1 de diseño antes de freeze; aceptación target e integración son gates separados, nunca aceptación implícita.

Sólo lifecycle finito y recuperación requeridos por PAPER, sin framework general de workflows. Temporal self-hosted se conserva como reserva. Si la solución necesita workflow extenso o difícil de demostrar, comparar de nuevo ingeniería, operación y seguridad frente a Temporal antes de ampliar el diseño.

G1/G2 se aplica según estado e incertidumbre: no nuevas entradas ante incertidumbre material; cancelar sólo entradas identificadas/verificadas con efecto seguro; preservar protectores. Agentes, scheduler o DB no activan G3 ni reanudan materialmente. Una DB no disponible puede impedir actuar incluso bajo G2: no eludir el audit/estado confiable.

## Alcance

No autoriza instalar servicios, configurar host, credenciales/cuentas, gasto, implementación u operación. No selecciona Strategy, datasets, umbrales o pin LEAN. `implementation_locked=true`, `TARGET_ACCEPTANCE_DEFERRED`, holdout `INTEGRITY_UNKNOWN`; main intacta. DoR no alcanzado. La revisión independiente prevista por §3.16 y las obligaciones de aceptación permanecen.
