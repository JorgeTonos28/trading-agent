# H10 — modelo finito de admisión y fencing

Protocolo previo2026-10-29. Enumerar interleavings de dos outputs, expiración/claim, cancelación, deadline y restore. Cada output es un punto de admisión atómica abstracta; el oráculo deriva elegibilidad del prefijo de historia, no de estado mutable compartido. Contrastar con modelo de estado y buscar contraejemplos deliberados al retirar fencing o unicidad del receipt. Repetir discovery de slots sin notificaciones prueba dedup por identidad en un modelo, no PostgreSQL.

Sin SQL/runtime/financial engine, threads, broker, estrategia o datos reales. No demuestra serialización de PostgreSQL, filesystem, WAL, clock real, crash durante SQL o suficiencia/capacidad. Una máquina finita de laboratorio no es autorización para construir un workflow general. Captura única; conservar cualquier discrepancia/contraejemplo.
