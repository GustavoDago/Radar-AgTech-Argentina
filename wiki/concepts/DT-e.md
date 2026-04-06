---
type: concepto
tags: [agtech/trazabilidad, argentina/senasa, operativo/logistica, tecnologia/sigsa]
sources: [https://www.argentina.gob.ar/senasa/tramites/emision-de-documento-de-transito-electronico-dt-e]
confidence: high
last_update: 2026-04-05
---

# DT-e: Documento de Tránsito Electrónico

## Definición
El **DT-e** es el documento oficial y obligatorio establecido por **SENASA** para amparar el traslado de animales vivos (bovinos, ovinos, porcinos, etc.) dentro del territorio argentino. Es la piedra angular de la trazabilidad sanitaria del país.

## Funcionamiento Técnico
- **Emisión:** Se realiza a través del sistema **SIGSA** (Sistema Integrado de Gestión de Sanidad Animal).
- **Validación:** El sistema verifica que el establecimiento de origen no tenga bloqueos sanitarios y que los animales cumplan con los requisitos de vacunación (ej. Aftosa, Brucelosis).
- **Vigencia:** El documento tiene una validez temporal limitada para el trayecto declarado.

## Interacción con la Identificación Electrónica
Con la entrada en vigencia de la [[Resolucion SENASA 841-2025]], la emisión del DT-e estará ligada a la lectura de los dispositivos RFID. 
- **Fricción Crítica:** Si un animal detectado en la lectura RFID no coincide con el stock declarado en SIGSA, el DT-e no puede ser emitido, bloqueando el despacho del camión.
- **Pain Point:** Las caídas del sistema SIGSA en zonas rurales sin conectividad impiden la emisión en tiempo real, generando sobrecostos logísticos.

## Oportunidad AgTech
- **Sincronización Offline:** Aplicaciones que permitan preparar el DT-e de forma offline en la manga y sincronizar con SENASA en cuanto haya señal.
- **Automatización:** Integración de lectores de bastón RFID con la API de SENASA para evitar la carga manual de caravanas en el formulario del DT-e.

---
**Temas Relacionados:**
- [[Resolucion SENASA 841-2025]]
- [[Pain Points de Trazabilidad]]
- [[Zonas Nucleo Adaptacion Tecnologica]]
