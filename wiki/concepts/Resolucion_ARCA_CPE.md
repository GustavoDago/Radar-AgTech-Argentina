---
type: concepto
tags: [arca, afip, sisa, cpe, logistica, carta_de_porte, regulacion, compliance]
sources: [aduananews.com, llbsolutions.com]
confidence: high
last_update: 2026-05-20
---

# Resolución General Conjunta ARCA 5821/2026 (Control Logístico Granario)

Establece las nuevas reglas de gobernanza y control fiscal para el transporte de granos dentro de la República Argentina, introducidas por **ARCA** (ex AFIP) en **2026**. Esta norma reorganiza por completo la emisión de la **Carta de Porte Electrónica (CPE)**, eliminando intermediarios y delegando la totalidad del control al estado registral de los operadores dentro del **SISA** (Sistema de Información Simplificado Agrícola).

## 1. El Latigazo Regulatorio y Cambios Clave
*   **Eliminación del RUCA:** Se descarta el Registro Único de la Cadena Agroalimentaria (RUCA) como requisito vinculante para documentar traslados físicos de granos. Todo el control se centraliza de manera exclusiva en las bases del **SISA**.
*   **Punto Único de Fallo (SPOF) en SISA:** Si un productor, acopiador, transportista o planta de destino pierde su estatus "Activo" en SISA por una inconsistencia registral o fiscal de último minuto, el sistema de ARCA bloquea inmediatamente la emisión de la CPE. La operación física se paraliza al 100%.
*   **Libertad de Destinos y Peso Máximo:** Aunque se flexibiliza la obligación de descargar en el acopio más cercano a la cosecha, se endurecen drásticamente las sanciones por transportar sobrecargas de peso o datos de choferes desactualizados, recayendo toda la responsabilidad penal e impositiva sobre el emisor del documento.

## 2. Fricciones Logísticas Monetizables (El "Pain Point")
*   **Inconsistencias de Stock SISA vs. Físico:** El sistema de ARCA autocalcula el saldo de granos teórico basado en las declaraciones de cosecha pasadas. Si el stock teórico en SISA es menor a la carga física del camión, el sistema emite un error impositivo y deniega la CPE. La mercadería se queda varada en el lote bajo la lluvia o en la banquina.
*   **El Infierno de las "Contingencias en Tránsito":** Ante una rotura mecánica, cambio de acoplado o re-ruteo imprevisto en ruta, el emisor debe ingresar al portal fiscal de ARCA a registrar manualmente una contingencia. Este proceso administrativo es complejo, requiere clave fiscal en áreas rurales con nula conectividad a internet, y su omisión genera la retención policial del camión en ruta.

## 3. Oportunidad SaaS: Mitigación de Fricción
*   **Capa de Pre-auditoría:** Las empresas agrícolas necesitan un software que simule el cálculo de stock de ARCA antes de mandar a cargar el camión, detectando inconsistencias registrales y de cubicación con antelación.
*   **Offline-First de Contingencias:** Una solución móvil que actúe en el celular del transportista sin internet, que registre la contingencia localmente (con prueba de foto geolocalizada) y la suba a ARCA en cuanto detecte señal 4G de forma automatizada.

## Backlinks
*   Ver impacto logístico en [[Friccion Logistica Exportadora]]
*   Ver tesis SaaS asociada: [[Terminal_Queue_Optimization_SaaS]]
*   Ver tesis SaaS asociada: [[SISA_Shield_SaaS]]
