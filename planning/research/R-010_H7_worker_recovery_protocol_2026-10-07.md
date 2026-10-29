# R-010/R-011 — H7: worker/retry durable sintético

Preregistro 2026-10-07, antes de ejecutar. Pregunta: ¿puede el motor Temporal candidato ejecutar una Activity, recuperar la pérdida abrupta de su worker y conservar un resultado lógico sin asumir exactly-once? H6 no ejecutó worker.

## Scope

Probe desechable, sin Trading OS, Codex/LLM, estrategia, broker, credenciales, órdenes ni datos financieros. Reutiliza Temporal CLI 1.9.1 ya descargado/verificado, servidor **development** local loopback con directorio TEMP nuevo. Python SDK 1.34.0 descargado como wheel/dependencias en TEMP dedicado, sin instalación/config global, service/task/admin/firewall. Registrar metadata/versiones y hashes de dependencias. Framework de workflow determinístico fuera de la capa AI restringida.

Activity sintética registra `activity.info().attempt` en fichero propio y espera antes de devolver contenido `authority=NONE`. Workflow configura schedule-to-close/start-to-close y máximo de intentos explícitos (valores del experimento, no política operacional). Controller inicia worker, espera marca de primera Activity, termina **su propio proceso worker**, inicia otro en mismo task queue y obtiene resultado. El primer worker no termina su Activity; el retry debe quedar observable. No copiar secrets/env completo a hijos. Server listen solo loopback; cleanup exclusivamente PIDs propios y TEMP absoluto verificado.

## Criterios antes de resultados

1. SDK/servidor/worker arrancan con versiones registradas y sin endpoints externos de ejecución.
2. Activity efectivamente entra y marca el primer intento antes de kill.
3. Segundo worker completa el workflow dentro de timeout global acotado.
4. Intentos observados incluyen reejecución después de pérdida del primer worker; historial refleja Activity completion y cierre, no confundir workflow tasks con Activity attempts.
5. Resultado `authority=NONE`, output lógico único del workflow; **no** afirmar una sola ejecución de Activity ni exactly-once de efectos externos.
6. Submission duplicada del resultado a ledger SQLite de receipt sintético externo tiene un solo receipt por job y rechazo duplicado; no DB financiera ni selección D-026.
7. Todos los procesos propios detenidos, TEMP de estado eliminado con paths verificados; dependencias reutilizables TEMP declaradas como residuos de investigación.

PASS/FAIL/ERROR por criterio; errores/import/network/version preservados. Un fallo del fixture no se etiqueta automáticamente rechazo del motor ni de S2-B. El SDK workflow sandbox no es barrera de seguridad de procesos. H7 prueba comportamiento del motor, no integración Codex, auth Plus, almacenamiento productivo, S2, host personal o capacidad PAPER.

## Reutilización y siguiente decisión

Temporal WRAP candidato del roadmap; APScheduler 3.x ADAPT alternativa (calendar no aporta recepción/fencing/ledger por sí solo); OS scheduler REFERENCE_ONLY. Resultado sirve para comparación D-025, sin seleccionar motor/deployment automáticamente. Producción no usar `start-dev` como sustituto del servicio endurecido; costes/setup/backup/transporte y permisos siguen scorecard.

Fuentes primarias consultadas: [SDK Python](https://github.com/temporalio/sdk-python), [deployments](https://docs.temporal.io/production-deployment), [self-host](https://docs.temporal.io/self-hosted-guide), [APScheduler FAQ](https://apscheduler.readthedocs.io/en/3.x/faq.html). Probe no añade runtime IA distinto de OpenAI/Anthropic.
