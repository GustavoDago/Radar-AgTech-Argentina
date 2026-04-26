---
type: oportunidad_especifica
target: Frigorifico Gorina
priority: ultra-high
date: 2026-04-19
---

# Análisis de Oportunidad: Gorina vs. Aftosa China

## La Fricción (El Dolor)
Gorina está creciendo en volumen mientras el resto de la industria se contrae. Este crecimiento, sumado a la amenaza de la cepa de Aftosa en China, crea una "Tormenta Perfecta":
1. **Saturación Operativa**: No pueden seguir registrando faena manualmente con el volumen actual.
2. **Riesgo de Default de Exportación**: Si China detecta una inconsistencia mínima, bloquea la planta. Gorina exporta miles de toneladas; un bloqueo de 30 días es catastrófico para su flujo de caja.

## El Moat (Nuestra Defensa)
Nuestra propuesta no es una base de datos, es un **Middleware de Validación en Tiempo Real**:
- **Tecnología**: Java/Spring Boot con integración directa a lectores RFID industriales (antenas fijas en riel de faena).
- **Lógica**: Cruce instantáneo de ID de animal vs. Protocolo Sanitario China (vacunación, origen, semáforo aftosa).
- **Diferencial**: No esperamos al cierre del lote para reportar errores; el sistema alerta en el segundo en que un animal sospechoso entra a la línea de faena.

## Análisis Escéptico (Tech Leader View)
1. **Riesgo de Hardware**: La línea de faena de Gorina tiene interferencias metálicas masivas. Si nuestras lecturas RFID fallan un 5%, el sistema es inútil. *Mitigación*: Necesitamos algoritmos de filtrado de ruido y redundancia de antenas.
2. **Resistencia de IT Interna**: Gorina debe tener su propio ERP (posiblemente un legacy robusto). No querrán un sistema nuevo. *Solución*: Venderlo como un **"Edge Gateway"** que solo inyecta datos validados al ERP vía API/Webhooks.
3. **Dependencia de Terceros**: Si SENASA (SIGSA) está caído por el desfinanciamiento reportado hoy, nuestra validación no tiene contra qué comparar. *Solución*: Caché local de estatus sanitarios y validación offline con firma digital.

## Acción Inmediata
- Contactar a la **Dirección de TI** de Gorina. No ofrecer "software", ofrecer un **"Shield Sanitario para el Mercado Chino"**.
