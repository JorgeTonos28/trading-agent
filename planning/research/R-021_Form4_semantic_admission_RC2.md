# R-021 — Form4: semántica, versiones y admisión — RC2

2026-10-14 · primera fuente externa candidata; ningún dataset/estrategia seleccionado, sin SEC contacts/API ni histórico de operaciones propio. E1 table-only se conserva. Nuevo trabajo offline extrae footnotes/flags y prueba límites, no simula paper.

## Hechos primarios que afectan2019–2022

[SEC guide](https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/insider-trading-arrangements-and-related-disclosures) fija cumplimiento de checkbox10b5-1 para filings desde2023-04-01. **Ausencia antes de esa fecha no demuestra operación sin plan.** [Form4/instrucciones actuales](https://www.sec.gov/files/form4.pdf) distingue tablas derivadas/no derivadas, P privado/open-market, precio sin brokerage costs, footnotes/exhibits y amendments que pueden añadir/corregir líneas sin repetir todas. [Techspec](https://www.sec.gov/submit-filings/technical-specifications) lista Ownership5.5 marzo2026, cambios de foreignsymbol/addresses; preservar versiones anteriores, no exigir campos actuales a historia.

Estas son fuentes de formato/reporting, no dictamen de legalidad ni evidencia de alpha. No etiquetar checkboxfalse como DISCRETIONARY probado, ni aplicar checkboxglobal sin relación a cada transaction row. Un formulario mixto puede necesitar footnote mapping; a falta de evidencia, row_plan_status=UNKNOWN. Schema-version/currentfiling enrich no reescribe historia.

## Estados propuestos

Conservar raw/rootflag y provenance, aparte de clasificación: TRUE_REPORTED / FALSE_REPORTED / MISSING / INVALID / CONFLICT; por fila PLAN_CONFIRMED / NON_PLAN_EVIDENCED / UNKNOWN. Reportedfalse no equivale a NON_PLAN_EVIDENCED. purchase_class=EXCHANGE_EVIDENCED/PRIVATE_EVIDENCED/UNKNOWN; códigoP no la decide. Excluir derivados para candidato equity, pero no perderlos del rawaudit. Footnote texto original+IDs+enlace a exhibits; referencia sin contenido no completa evidencia.

E-SEC-01 EdgarTools pin5.62.0 ofrece `Footnotes.extract` y parser de flag; comprobar offline antes de confiar. Invalid/missing no defaultsFalse; investigar si acepta casing/lexical forms y unknown. Clasificador de lenguaje no constituye barra de seguridad ni signaltruth: phrases negadas/conflictivas/mixed/foreign/xmlnamespace y references rotas mantienen UNKNOWN. Reglas de interpretación candidatas se preregistran; LLM no completa signal operativa.

## Opciones de candidata sin waiver PIT

S-F4-01 original exige contexto/plan suficiente: si historia2019–2022 no permite acreditar filtro, **NO_ADMITTED_FOR_HISTORICAL_COMPARISON**, no rechazo económico. Conservar research/prospectivo. Variante nueva plan-agnostic podría usar compra admisible sin claim de discretionary, con unknown explícito y otra hipótesis/config; debe registrarse como variante y cumplir clocks/rights/semántica/riesgo. No cambiar S-F4-01 silenciosamente para ganar coverage ni abrir2023+ reserva para elegirla.

Amendment publica nueva vista desde availability nueva; doc4/A puede ser parcial, no snapshot completo del original. Aún requiere mecanismo de vincular original/línea económico con evidence, mappingCIK/instrument/security as-of/owners-dedup y canalavailability. Receipt prospectivo no prueba pasado. Confidencialidad/historia/delistings/clocks/rights y benchmark equity por universo propio permanecen gates, no resolved por parserPASS.

## Build-vs-Reuse y criterios de probe

Biblioteca públicaMIT candidata ADAPT/WRAP; rawfootnotes/flag parser REUSE_AS_IS sólo si pruebas/scope lo justifican, seleccionadoNO. Código0/ops/mapping/historia UNKNOWN y seis campos económicos del dossierE1 vigentes; no frontendMCP o runtime nuevo. Probe usar fixtures sintéticos y no factory con enrichment, ni contacto falso. Nulos/conflictos/negaciones/plan global/amendmentpartial/reference ausente deberán quedar identificables; gate dataset/PIT permanece NOT_TESTED.

## Histórico/dissemination — wave06

[Histórico/dissemination](R-021_SEC_availability_admission_RC3.md) añade especificación y límites; Q057 aprobado en paquete, Q058 números propuestos. Sin fuente/modelo/Strategy admitidos ni performance. E4 sólo cálculo/meanpilot, no cobertura CAGR/ES/DD; M11 parcial/holdoutUNKNOWN. Versiones/declaraciones anteriores conservadas, no rehash histórico.
