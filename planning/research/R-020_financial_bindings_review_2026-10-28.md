# Revisión crítica independiente — bindings y stack

2026-10-28, roadmap§3.16. Revisor `independent_hardening_review`, sólo lectura, fuentes/hashes/aritmética; sin API de datos, cuentas, probes, edición o aprobación de decisiones. Complementa revisión de proveedores del mismo día.

## Hallazgo material reparado

P1: D1 decía dimensionar antes de seleccionar stack, pero Q-063 proponía dirección con UNKNOWN. Se aclara trazablemente en ambos documentos: la decisión solicitada sólo selecciona dirección de familias/huella condicionada. Configuración, envelope nominal/ráfaga/estrés, latencias, RPO/RTO, retención y prueba de suficiencia permanecen P1 antes de freeze; H9 no los satisface. No cierre de D-025/026/pin/suficiencia por una elección de familias.

El revisor no encontró otro P0/P1 que impida presentar Q-063 **en ese alcance condicionado**. B3 no admitido es impedimento real de entradas, no sólo prueba target. G1+G2 y B-RT1 sin permisos nuevos. Datos derivados/rights, volumen/dividendos/PIT conservan gates. Caps sólo sobre uso incremental/baseline fijo y precondiciones afines; no se omite cartera existente. Comparación de workflow explicita mayor ingeniería en C con APS y no impone WSL/VM/admin.

## Evidencia y límites

Verificó diez hashes de fuentes del paquete y cinco DLL observadas; QL3 es build/metadata, no ejecución del engine. H9 demuestra transacciones/fixtures y receipt perdido; el complemento lee realmente copia restaurada pero sus guardas no son recuperación operacional ni seguridad de anchors. No PostgreSQL, FSYNC/power-loss, carga PAPER o aceptación target por este review.

Precisión menor incorporada: DA-S2 no ejecutó timezone parsing/DST aunque lo mencionara el protocolo; queda NOT_TESTED en scope/protocolo, sin nuevo probe ni alteración de captura. Los marcadores declarativos B3/R4 se separan de checks calculados. Ninguna suma de PASS ni revisión reemplaza datos/método/Strategy/operación.

Decisiones del propietario pendientes: Q-063, posteriormente las restantes materiales cuando exista evidencia. D-011, configuración financiera, datos/B3, parámetros y DoR siguen abiertos; implementación bloqueada, target diferido, holdout desconocido.

## Revisión complementaria de pin/archivos

El revisor verificó después el hallazgo QL4 y capturas QL5: fallo real de containment del helper dentro del laboratorio propio, no explotación financiera/S2 ni atribución automática al advisory DotNetZip. Auditoría41libraries incluye proyectos;7 pares paquete/advisory corresponden a5advisories únicos, no SBOM completo.

QL5 conserva ambos timeouts60.396s/120.144s, sin smoke o filas ejecutadas. La factibilidad integrada es inconclusa, no incompatibilidad probada. Hash del controlador02 y enlace a captura01 coinciden. Propagación revisada en registro/riesgos/readiness/master sin error material nuevo: pin es obligación P1, sin aceptación o rechazo de familia. Q063 no concede waiver/instalación.

[QA final de coherencia](financial_phase_final_QA_2026-10-28.json):65 controles PASS de hashes/estados/formatos/aritmética/referencias, **no65 controles financieros ni seguridad aceptada**. Incluye como hechos el FAIL del helper y los ERROR de build. La captura inicial de51 controles anterior a esta ampliación se conserva; ninguna prueba de mercado o estadística se ejecutó en QA.
