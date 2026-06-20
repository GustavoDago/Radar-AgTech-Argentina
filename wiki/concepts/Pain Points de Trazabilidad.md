---
type: concepto
tags: [agtech/trazabilidad, operativo/pain_points, ganaderia/rfid, tecnologia/sigsa]
sources: [industry_reports, market_feedback, daily_summary_2026-06-20, hackathon_agroactiva_2026]
confidence: high
last_update: 2026-06-20
---

# Pain Points de Trazabilidad: RFID y SIGSA

## Fricciones Identificadas
1. **Caídas del SIGSA:** La dependencia del sistema central de SENASA para emitir el [[DT-e]] genera retrasos en la carga de camiones en establecimientos con baja conectividad.
2. **Sincronización Crítica (Hackatón Agroactiva 19/06/2026):** Se detectaron fallas masivas en la sincronización en tiempo real entre los lectores RFID de campo y la base de datos central de SIGSA. Los dispositivos a menudo "no son reconocidos" por el sistema estatal a pesar de estar correctamente grabados, bloqueando la emisión de DT-e.
3. **Brecha de Adopción Generacional:** Resistencia técnica en operarios de campo para el manejo de interfaces digitales complejas, lo que deriva en errores de lectura y pérdida de datos.
4. **Deterioro Operativo de SENASA:** Se reporta que el organismo no puede utilizar gran parte de sus propios recursos, profundizando su deterioro operativo. Esto aumenta exponencialmente el riesgo de fallas sistémicas en SIGSA.
5. **Fallas en la Lectura RFID:** Los lectores de baja frecuencia (RFID LF) pueden presentar interferencias en corrales de metal o balanzas electrónicas, ralentizando el movimiento de hacienda.
6. **Inconsistencias en la Recuperación en Faena:** Los frigoríficos enfrentan el desafío de recuperar dispositivos (microchips o bolos) durante la línea de faena para evitar contaminación física del producto.

## Desafíos de Cumplimiento (Actualizado Junio 2026)
- **Resolución 841/2025:** Ratificada en el Boletín Oficial (19/06/2026). Obligatoriedad de lectura electrónica para todos los movimientos a partir del 1 de enero de 2026. La falta de infraestructura (lectores, conectividad) y la inestabilidad de SIGSA son cuellos de botella críticos.
- **Auditorías Externas:** Necesidad de reportes instantáneos para auditorías de la Unión Europea sobre el origen electrónico del animal.
- **Diferenciación por Calidad:** La necesidad de vincular datos de marmoleo (ver [[Cabana Buen Retiro]]) con el ID individual para capturar primas de precio en exportación.

## Oportunidades de Venta Directa
- **Middleware de Sincronización:** Software que actúe como buffer entre el hardware RFID y SIGSA, permitiendo validaciones offline y subida diferida de datos.
- **Interfaces de Usuario Simplificadas:** Apps móviles diseñadas para uso rudo en manga con UX minimalista ("un solo botón").
- **Integración Genética:** Módulos que vinculen el [[Resolucion SENASA 841-2025]] con índices de calidad de carne para capturar el sobreprecio en mercados de exportación.

## Backlinks
- Ver normativa en [[Resolucion SENASA 841-2025]]
- Ver clientes potenciales en [[Zonas Nucleo Adaptacion Tecnologica]]
- Casos críticos: [[Frigorifico Logros]], [[Consorcio de Frigorificos ABC]]
