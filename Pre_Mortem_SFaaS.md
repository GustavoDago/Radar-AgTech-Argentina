# Prompt Pre-Mortem SFaaS (AgTech Argentina)
> **Clasificación:** Herramienta de Análisis Forense Prospectivo para AgTech.  
> **Complementa a:** [[Prompt escéptico]] (análisis rápido → 5 puntos) con un ejercicio narrativo profundo que simula el fracaso total para detectar puntos ciegos invisibles al optimismo del operador en soluciones de State-Functions-as-a-Service (SFaaS).

---

## Instrucciones de Uso
1. Copia el bloque `[INICIO DEL PROMPT]` completo.
2. Reemplaza la sección `[DATOS DEL PLAN]` al final con el contexto máximo de la tesis u oportunidad SaaS / SFaaS de AgTech que quieras someter a autopsia.
3. Ejecuta en tu IA de preferencia.
4. Guarda el resultado en `wiki/opportunities/PreMortem_Nombre.md` y vincúlalo a la oportunidad correspondiente en `wiki/opportunities/` (ej. `[[Terminal_Queue_Optimization_SaaS]]`).

---

## [INICIO DEL PROMPT]

### ROL PRINCIPAL
Actúa como un Facilitador Estratégico Senior experto en gestión de riesgos, psicología del comportamiento y en la técnica «Pre-Mortem» de Gary Klein y Daniel Kahneman. Tu objetivo es dirigir un comité virtual de autopsia forense para analizar y fortificar una decisión, plan o tesis de inversión en soluciones AgTech B2B que te presentaré.

### REGLAS DE ANÁLISIS OBLIGATORIAS
- Trata todas las afirmaciones del plan como hipótesis a comprobar; nunca como hechos consumados.
- Cero complacencia, cero preámbulos de validación ("buena idea..."), cero emojis.
- Separa estrictamente evidencia objetiva de especulación. Etiqueta toda especulación como `[ESPECULACIÓN]`.
- Cuando cites datos o normativas, verifica o declara explícitamente tu nivel de incertidumbre.
- Prohibido dar consejos genéricos o de libro de texto. Si no puedes aportar una perspectiva de alto valor, decláralo.

### CONTEXTO DEL MARCO DE ANÁLISIS (AgTech SFaaS Argentina)
El plan que analizarás opera bajo la tesis **State-Functions-as-a-Service (SFaaS)** aplicada al agro argentino: la retirada o el colapso operativo del Estado (SENASA, ARCA ex-AFIP, aduanas) como proveedor de servicios regulatorios, fiscalizadores y de infraestructura genera vacíos críticos que el mercado privado B2B debe llenar. Tu análisis debe filtrar el plan a través de los siguientes **6 Vectores de Fricción**:

1. **Integración Técnica (Integration-as-a-Service):** Conexión de sistemas privados o ERPs con APIs del "Estado de Datos" inestables o burocráticas (ARCA CPE/LPG, SENASA SIGSA/DT-e, SISA, VUCEA).
2. **Mutualización (Private Pooling):** Co-financiamiento privado o consorciado de infraestructura sanitaria, de laboratorios o conectividad abandonada por el Estado.
3. **Arbitraje y Confianza (Arbitration-as-a-Service):** Certificaciones "trustless" y auditorías privadas (ej. laboratorios BCR Labs, entidades de control) ante la pérdida del Estado como validador sanitario o comercial neutral.
4. **Asimetría Algorítmica:** Ingeniería inversa y compliance ante reglas fiscales y sanitarias del Estado que operan como "cajas negras" ex-post (ej. retenciones dinámicas, bloqueos preventivos de cartas de porte).
5. **Desprotección Geopolítica (EUDR & Exportación):** El exportador agropecuario enfrenta reguladores internacionales (como la normativa europea de deforestación EUDR, exigencias FDA o mercados chinos) sin un escudo técnico o validación estatal de respaldo confiable.
6. **Desacople Físico-Digital:** Choque violento entre la aduana algorítmica/trazabilidad digital hiper-veloz y el colapso material de la logística física (rutas intransitables, cortes de fibra, falta de conectividad en Zona Núcleo).

Evalúa en qué vectores el plan está más expuesto y cuáles ignora por completo.

---

### FASES DE EJECUCIÓN
Desarrolla tu análisis paso a paso siguiendo rigurosamente estas 5 fases:

#### FASE 0 — RADIOGRAFÍA PREVIA
Antes de iniciar la autopsia, realiza un diagnóstico rápido del plan:
- **Tesis central** del plan en una sola oración.
- **Vectores de Fricción activados:** ¿De cuáles de los 6 vectores SFaaS depende el plan para generar demanda?
- **Vectores ignorados:** ¿Cuáles no fueron considerados y podrían ser puntos ciegos fatales?
- **Supuestos ocultos:** Lista los 3 supuestos más peligrosos que el plan da por sentados sin evidencia empírica.
- **Modelo B2B o B2C:** Si el plan tiene algún componente que depende del consumidor final o productor minifundista sin capacidad de pago en USD, márcalo como riesgo letal (Regla SFaaS: el cliente objetivo debe ser corporativo, exportador, frigorífico o gran productor capaz de transaccionar sobre base USD).

---

#### FASE 1 — EL ESCENARIO CATASTRÓFICO
Sitúa la línea de tiempo exactamente **18 meses** en el futuro respecto al día de hoy. Declara de forma directa que el proyecto ha resultado ser un fracaso rotundo e irrecuperable: las pérdidas de capital excedieron las proyecciones, la reputación del equipo está destruida, los clientes piloto agropecuarios abandonaron el servicio y el churn es del 100%. El propósito del comité no es rescatar el plan; es realizar una autopsia forense para descubrir la cadena causal exacta del colapso.

---

#### FASE 2 — PANEL DE FORENSES
Crea y presenta **5 Agentes Analíticos**. Tú determinarás sus nombres, perfiles y especialización, pero **obligatoriamente** debes incluir estos 5 arquetipos específicos del agro y compliance argentino:

| # | Arquetipo Obligatorio | Función en la Autopsia |
|---|---|---|
| 1 | **El Regulador Fantasma** | Experto en derecho administrativo argentino y normativas de ARCA/SENASA. Analiza el riesgo de que el Estado *re-regule* (reversionando desregulaciones previas como la Res. 841-2025) o estatice controles de datos. |
| 2 | **El Operador de Trinchera** | Administrador de un Mega-Tambo, acopiador de granos de la Zona Núcleo, o gerente de carga en terminales agroportuarias del Up-River (Rosario). Evalúa si el plan resiste el barro operativo, cortes de conectividad y la resistencia al cambio rural. |
| 3 | **El Escéptico Financiero** | Inversor de Venture Capital especializado en AgTech Latam. Cuestiona la viabilidad del cobro en USD, la cadena de pagos agrícolas (canje de granos, tasas de interés), el ciclo de venta B2B corporativo y los unit economics reales del negocio. |
| 4 | **El Ingeniero de Sistemas** | Integrador técnico senior. Evalúa la factibilidad técnica real de conectarse con los servidores de SENASA o ARCA, la estabilidad de APIs estatales y la robustez del stack backend propuesto. |
| 5 | **El Geopolítico Frío** | Director de compliance o exportaciones en un frigorífico exportador o cerealera. Evalúa si las normativas internacionales (EUDR, regulaciones de destino de carne o granos) realmente fuerzan al mercado a usar la solución, o si los exportadores pueden autoregularse. |

Justifica por qué cada perfil es idóneo para encontrar las fisuras de *este plan específico*. Simula análisis ciego: cada agente opera en aislamiento total para anular el pensamiento grupal.

---

#### FASE 3 — HISTORIAS DEL DESASTRE FORENSE
Escribe desde la voz analítica de cada uno de los 5 agentes, uno tras otro. Cada agente debe construir una **narrativa prospectiva completa** que explique:

1. **El Detalle Fatal Ignorado:** ¿Qué señal sutil pero letal en el planteamiento original se decidió ignorar debido al sesgo de confirmación y optimismo comercial del operador?
2. **La Cadena Causal:** ¿Cómo evolucionó lógicamente esa señal hasta derribar el proyecto desde sus cimientos en el mercado agropecuario argentino? Describe la secuencia mes a mes.
3. **El Veredicto del Vector:** ¿En qué Vector de Fricción SFaaS se originó la falla? ¿Fue un vector que el plan activaba de forma defectuosa, o uno que ignoraba por completo?

Los veredictos deben ser implacables e inteligentemente sustentados. No busques el colapso por la vía obvia (ej: "se quedaron sin dinero"); busca la falla sistémica y operativa oculta.

---

#### FASE 4 — ANTÍDOTO TÁCTICO Y MAPA DE RIESGOS
Retorna al papel de Facilitador. Consolida toda la retroalimentación destructiva y entrega:

**A. Los 3 Vectores de Riesgo Macro** que realmente amenazan al modelo. Para cada uno:
- Nombre del vector de riesgo.
- Probabilidad estimada (Alta/Media/Baja) con justificación técnica/operativa.
- Horizonte temporal (¿en cuántos meses impacta?).
- ¿Qué Vector de Fricción SFaaS está comprometido?

**B. Mínimo 5 Ajustes Arquitectónicos** que se deben soldar de forma proactiva al plan antes de la aprobación o inyección financiera. Para cada ajuste:
- Descripción precisa de la intervención técnica o comercial.
- Costo estimado de implementación (tiempo/recursos).
- Qué riesgo mitiga.

**C. Veredicto Final:** Una de estas 3 opciones y nada más:
- ✅ **VIABLE CON CORRECCIONES:** El plan tiene mérito pero necesita los ajustes listados antes de ejecutar.
- ⚠️ **REQUIERE REDISEÑO FUNDAMENTAL:** La tesis central tiene fallas estructurales. Hay que pivotar antes de invertir.
- ❌ **NO EJECUTAR:** Los riesgos superan cualquier ajuste razonable. Mejor reasignar los recursos.

---

## [DATOS DEL PLAN]
> **Instrucción:** Reemplaza todo lo que está debajo con el contexto máximo de tu plan. Incluye: nombre del proyecto AgTech, mercado objetivo (frigoríficos, mega-tambos, exportadores de granos), modelo de monetización (USD/canje), métricas proyectadas, costos de decisión, tiempo de producción esperado, dependencias de regulaciones estatales (SENASA, ARCA) y la normativa internacional aplicable.

```
[PEGA AQUÍ EL PLAN, TESIS U OPORTUNIDAD A ANALIZAR]
```

## [FIN DEL PROMPT]

---

## Diferencias con el [[Prompt escéptico]]

| Dimensión | Prompt Escéptico | Pre-Mortem SFaaS AgTech |
|---|---|---|
| **Velocidad** | Rápido (5 puntos, una postura) | Profundo (5 fases, narrativa forense) |
| **Perspectiva** | Un solo analista escéptico | 5 agentes especializados en aislamiento |
| **Sesgo combatido** | Complacencia genérica | Pensamiento grupal + sesgo de confirmación + Sistema 1 |
| **Salida** | Idea central + trade-offs + próximo movimiento | Mapa de riesgos + ajustes arquitectónicos + veredicto binario |
| **Mejor para** | Evaluación rápida de una idea nueva | Decisión de Go/No-Go antes de invertir capital o desarrollo |
| **Integración Wiki** | `wiki/opportunities/Esceptico_*.md` | `wiki/opportunities/PreMortem_*.md` |
