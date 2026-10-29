# Wave08 — revisión crítica independiente y remediación

2026-10-15. Mandato roadmap§3.16. Reviewer independiente reutilizado, lectura exclusiva de documentos/source/result/metadata; no ejecución, instalaciones, históricos, cuentas, órdenes o aceptación target. Plan Architect conserva responsabilidad y QA. Complementa reviewwave07, no aceptación estadística global.

## Hallazgos y cambios

| Prioridad | Hallazgo concreto | Remediación |
|---|---|---|
| P1 | Borrador de checkpointDD añadía d_obs≤0 como veto histórico además deupperCI de esperanza, presentándolo como mera realización; nueva pregunta innecesaria para investigar DD-E | Se elimina veto antes de usarlo; d_obs reporte. ADR020 condición2 ya autoriza investigación candidata. [Nota](D-011_drawdown_claim_checkpoint_RC0.md) deja trazabilidad, no ownergate activo ni elección por silencio |
| P1 | Fresh/carry confirmatorio podía elegirse enF1 después de observar selección | Regla fresh/flat en ambas fases y carry sólo sensibilidad antes deF0; F1 materializa, no selecciona reset. JSON/declaración inicial y textos corregidos sin trials/resultados de mercado |
| P2 | make_qty1.x default redondea bancario y puede superar qty autorizable | Floor/round_down explícito en contrato/hipótesis; [QE1](probes/r009-nautilus-artifact/README.md)5/5 componente:1.6→default2/floor1. No adapter ni QP6 aceptado |
| P1 incorporación preventiva | G2 cancelparent puede cancelarchildren; evidenciaFIX no prueba TWS | [BrokerRC2](R-007_protection_dependency_contract_RC2.md) exige grafo/efecto verificado, no emergencystop/cierre implícitos; B3 sigueNOT_TESTED |

No P0 detectado en el paquete revisado. La revisión no autoriza d_obs veto ni DD-E final/predictivo: un cambio final material de claim se gobierna con evidencia. No requiere otra preferencia M1/K2/G-R1 ahora.

## Evidencia revisada en su alcance

- E7source/result coinciden con hash;14/14 propiedades aritméticas, media.148 sólo de6paths ficticios. No incertidumbre/α/potencia/modelo aceptados.
- QE0fuentes/resultados coinciden:2PASS2ERROR→4PASS1ERROR→6PASS0ERROR. Import/init/dispose vacío, no run/paridad/estrategia. ModeloEquitywhole no implica limitación delbroker.
- W0cota45días calendario no prueba sesiones/coverage; seis subcards siguenNOT_ADMITTED y no fullwarmupenero2005.
- IUT/AND no independencia deendpoints, no intervalos simultáneos y familia sinreset se distinguen enRC6.
- G1+G2/ADR006/015, sinG3/authorityLLM, reservaUNKNOWN/lock/targetdeferral preservados.

ADR021 y condición adicional del propietario fijan nominal10k y costes en5escalas obligatorios; no funding/gasto, no gatePASSuniversal añadido. Consultas proveedor están preparadas, **no enviadas**; autorización/remitente personal necesarios antes de contactar. Revisión final de reparaciones/esta nueva condición se registra en el cierre del hito, sin convertir review documental en datasets/métodos/engine aceptados.

## Cierre independiente confirmado

El reviewer confirmó reparaciones y ausencia de P0/P1 que impida cerrar **wave08 como hito de planificación/research**. Los hashes QE1 fuente/resultado/launcher coinciden; nominal10k/costes5escalas y consultas no enviadas están acotados. No cierreD011/método/data/broker/engine/Strategy/F0/DoR. Una respuesta/licencia personal futura no autoriza usoTeam/INFOTEP automáticamente. Trabajo independiente puede continuar; siguiente evidencia externa requiere acción de comunicación legítima.
