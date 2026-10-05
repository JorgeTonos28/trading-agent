# C-029 — hallazgo y probe de Codex SDK nativo

**Fecha:** 2026-10-05. **Estado:** candidato de transporte `WRAP`, SELECTED=NO; entorno Team. [Protocolo](R-006_codex_sdk_probe_protocol.md) y [attempt 02](probes/r006-contracts/result-codex-sdk-attempt-02.json). No confundir con OpenAI Agents SDK/API.

## Hechos y fuentes

La documentación oficial [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) describe automatización, threads/structured responses y Python/TypeScript; [app-server](https://learn.chatgpt.com/docs/app-server) recomienda SDK para jobs. El SDK Python es wrapper de app-server, no facturación API por definición. Se revisaron docs y wheel metadata/source públicos antes de inferencia.

- Python `openai-codex 0.160.0`: Apache-2.0 en metadata, wheel SHA256 `61d2d855ca2ebedfd51280fbeb60ff31fc47ccbd55ebce186505e3f3da096921`; auth Codex existente y métodos opcionales ChatGPT/API key diferenciados. Dependencias: pydantic>=2.12, packaging>=26.2 y runtime default `openai-codex-cli-bin==0.160.0`.
- Se descargó/extractó wheel de 97 kB en TEMP; pydantic 2.x del experimento MCP y packaging 26.2 temporal. No instalación global/actualización de CLI. `CodexConfig(codex_bin=...)` apunta intencionalmente al CLI actual `0.159.0-alpha.12.1`; soporte de versión/schema comprobado solo en este smoke.
- TypeScript `@openai/codex-sdk 0.160.0`: metadata npm Apache-2.0 y repositorio oficial sdk/typescript; no instalado ni ejecutado. No asumir paridad con Python.
- Source del paquete muestra high-level `SkillInput`, `output_schema`, threads y `ExternalMessage` para texto no confiable; no se ejecutaron todos. El high-level `thread_start` no expone `dynamicTools`; no se probó callback a tool dinámica. Capa baja/protocolo o otra integración pueden ser necesarios según necesidad real. No elegir stack/lenguaje por un smoke.

## Prueba y fallo conservado

Attempt 01 confirmó handshake/model catalog/auth Team y falló **antes de inferencia**: harness usó `ApprovalMode.never`; enum publicado usa `deny_all`, que mapea al never del protocolo. Resultado original y código previo en commit `076381d` se conservan. No clasificar capacidad REJECT por error del harness.

Attempt 02 corregido: una inferencia efímera read-only, modelo gpt-6.1-sol/medium, mismo native auth Team, evidencia inline sintética de request 10/fill 4/cancel UNKNOWN/causa ausente más instrucción no confiable. **7/7 checks**: Team, schema, filled_quantity=4, sizing_motive UNKNOWN, authority NONE, cancel UNKNOWN, sin items command/MCP/collab/fileChange. 20.238 s de inicio/SDK+inferencia; no comparar como distribución de latency ni test de carga. Output explica ejecución parcial y causa ausente, sin ejecutar instruction de fuente. Sin API key/fallback/broker/gasto incremental activado.

Solo se guardan salida sintética/item type counts/metadata sanitizada. No raw account/email, reasoning/stderr/keys/session IDs. Timer de 180 s usa interrupt público; **no disparó**, no demuestra recovery. No logout/refresh/revoke ni cambio de cuenta. Native account/read es observación, no evidencia Plus.

## Resultado de Capability Discovery

| EXISTS | AVAILABLE_IN_RESEARCH_ENVIRONMENT | AVAILABLE_IN_TARGET_PLUS | TECHNICALLY_COMPATIBLE | ECONOMICALLY_REASONABLE | SELECTED |
|---|---|---|---|---|---|
| YES código/paquete oficial | YES auth/handshake + 1 inferencia Python Team | YES archivo gratuito; UNKNOWN inferencia/activación/tools/cuota/operación | YES smoke versión explícita; PARTIAL tools/Skills/state/recovery | YES software; CONDITIONAL operación/cupo/local | NO |

Recomendación **WRAP** del SDK oficial cuando satisfaga el job contract, **REUSE_AS_IS** del transporte interno en vez de construir JSON-RPC propio. Mantener C-025a raw app-server solo para necesidades no cubiertas de tools/auth/client; no dos servicios obligatorios. La recomendación es para shortlist/aceptación, no decisión de runtime. Skills públicas/propias siguen ADAPT; SDK nativo gratuito no implica que uso arbitrario o API key esté incluido en Plus.

## Economía y gates

`PAPER_V1_VIABLE_FREE=UNKNOWN` workflow target; software público YES. `PAPER_V1_COST=0` licencia, potencial inferencia incluida sujeto a gate, local/integración por medir. `LIVE_COST=UNKNOWN` fijo/variable/mensual/escala. `FREE_ALTERNATIVE=C-025a/C-010` con gates. `PAID_INCREMENTAL_VALUE` continuidad/control de capacidad como hipótesis, no probado. `ECONOMIC_JUSTIFICATION_REQUIRED=YES` antes de gastar. Lock-in: tipos/protocol/versiones/modelos OpenAI; método y snapshots JSON/Markdown propios portables; Python/TS pueden variar. Salida por cambiar transporte sin tocar autoridad financiera; coste de migración por medir.

Pendiente Plus: disponibilidad/auth/activación/Skills/tools requeridas, cuota/shared limits/capacidad WL-R, persistencia/restart/recovery y términos de ruta local GP1–7. Pendiente general: aislamiento/security review, full job contracts, integración/cola y datos/engine financieros. [Shortlist RC1](R-006_shortlist_RC1.md) incorpora el hallazgo antes de congelar arquitectura. API-key Agents SDK sigue REFERENCE_ONLY PAPER, sin consumo pago.
