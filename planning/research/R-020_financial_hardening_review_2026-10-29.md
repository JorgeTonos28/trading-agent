# Revisión crítica independiente — financial hardening wave13

2026-10-29. Solicitada al agente independiente `independent_hardening_review` conforme al roadmap §3.16. Sólo lectura/diff/hashes; no laboratorios, edición, aprobación humana o aceptación operacional. El Plan Architect incorpora los hallazgos y conserva los pendientes.

## Hallazgos y resolución

| Hallazgo | Severidad de revisión | Resolución trazable |
|---|---|---|
| ADR024 correcto, pero encabezado vigente/readiness17 seguían solicitando Q063 | P1 coherencia | Encabezados históricos y checkpoint18 activo; approvalcommit9dbc255. No repetir aprobación |
| Q064 pedía permiso para estudiar, algo ya autorizado | P1 gobierno | Pregunta actual elige dirección de política tolerable PF versus exigencia nativa, no permiso de investigación. Ninguna ventana/orden admitida por propuesta |
| Pending se confundía con brecha material y exit ante incertidumbre | P1 seguridad financiera | Sólo futuro perfilPF puede distinguir transición conocida de incidente y definir tabla de commands; ahora fail-closed. Incertidumbre no permite emergencyexit; no G3 ni auto-resume |
| G1 no impide fills del remainder que sigue en broker | P1 riesgo financiero | Worst-case reachable quantity/gap antes de envío y durante instalación/cancel-race; reservas hasta confirmación, no sólo shortfall actual |
| QL7 cambio innecesario de paths relativos a absolutos | P1 compatibilidad de pin | QL8 conserva Path.Combine legacy y contrasta shape/contenido relativos en host mínimo. Callers no ensayados siguen gate |
| D2 no fijaba denominador de3jobs semanales | Precisión no bloqueante | Pico explícito53jobs/66attempts con13reserva, adicionales al50/63diario. Propuesta ex ante, sin entitlement |

## Evidencia revisada y límites

QL6 build133.473s y8checks incluye segundohelperFAIL, no seguridadPASS. QL7 conserva ERROR01/FAIL02 y9PASS03 tras normalizar fixture. QL8 conserva buildERROR01 por omitir Common/Data de código;02repone1171.cs conhashes, build110.57s/run1.178s/14PASS sinMain/Engine/Algorithm. Revisor verificó1171/1171hashes añadidos, controladores01/02, referencia a captura01, parcheCompression y tresDLL; coinciden. CapturasUTC originales coherentes; no fechas inventadas.

H10=840interleavings abstractos (7!/3!) y contraejemplos de mutaciones; no SQL/thread/PG. R5exposición24% del ejemplo y gap7.5%NAV correctos; no umbrales aprobados. D2 crashlocal0 pérdida de commit reconocida, desastreRPO300 y restoreaPAUSED3600 son propuestas diferentes, no garantías de hardware o protección.

**Conclusión independiente:** después de las correcciones, no nuevos P0/P1 que impidan presentar Q064 con alcance condicionado. La revisión no aprueba PF, perfil numérico, pin, PostgreSQL, Strategy, target o operación. Persisten los gates de checkpoint18 y masterRC0.
