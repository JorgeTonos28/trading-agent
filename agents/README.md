# Paquetes de roles — candidato RC0

Estos paquetes contienen **instrucciones y contratos de planificación**, no implementaciones ni agentes residentes. La raíz mantiene reglas globales; cada carpeta especializa el trabajo permitido dentro del Preparation Program. Runtime, activación operacional, sesiones/proyectos y subagentes siguen abiertos en D-024.

| Paquete | Función | Estado durante preparación |
|---|---|---|
| onboarding | Inventario, diferencias, acciones y readiness | Bootstrap Mode de Plan Architect |
| plan-guardian | Integridad frente al futuro plan congelado | DORMANT_UNTIL_FREEZE; hoy Plan Architect |
| quant-research | Metodología, PIT, costes/OOS y evaluación | Revisión/investigación; sin promover Champion |
| market-research | Fuentes, señales externas e hipótesis | Research; sin señales operativas |
| portfolio-manager-shadow | Propuestas hipotéticas y comparación | Diseño/probes; futura autoridad NONE |
| pedagogical | Explicación factual y aprendizaje | Diseño/probes; sin autoridad financiera |

Cada `package.json` declara ID/version/cwd/instrucciones/contratos/procedimiento candidato/dependencias/autoridad. Las referencias apuntan al repo completo; **independiente como unidad de rol no significa standalone sin shared/root**. No duplicar reglas o schemas que ya tengan fuente canónica. [Shared](../shared/README.md) es el catálogo común.

Manual: abrir carpeta dentro del Git root y verificar cadena de instrucciones/discovery antes del smoke. Programático: resolver paths desde repo root, asignar rol confiable, verificar hashes/versiones, cargar mismas instrucciones/contratos y validar outputs fuera del modelo. `AGENTS.md` no configura ACL ni concede acceso a herramientas.
