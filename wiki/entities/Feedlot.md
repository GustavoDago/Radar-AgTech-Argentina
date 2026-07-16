---
type: entity
category: actor_mercado
sector: ganaderia_bovina
escala: [pyme, grande]
digitalización: baja_media
---
# Feedlot (Engorde a Corral)

El **Feedlot** o establecimiento de engorde a corral es el eslabón de **confinamiento intensivo** entre el criador extensivo de terneros y el frigorífico. En Argentina operan aproximadamente **4.000 feedlots habilitados** por SENASA (muchos más informales), que engordaron más de **3,5 millones de cabezas** en 2025, representando cerca del 55% de la faena bovina nacional. Es un actor de altísima intensidad de datos — sanidad, nutrición, costos de conversión, trazabilidad — pero con una digitalización real sorprendentemente baja para su escala operativa.

## Perfil Operativo

| Variable | Detalle |
|---|---|
| Escala típica | 500 a 50.000 cabezas simultáneas |
| Ciclo de engorde | 90 a 150 días |
| Costo principal | Ración (60-70% del costo total) |
| Regulación clave | SENASA (habilitación, DT-e, Res. 841/2025) |
| Destino | Frigoríficos exportadores y consumo interno |

## Mapa de Empatía (Dolores y Fricciones 360°)

### 1. Gestión Sanitaria: El Riesgo más Caro
* **El dolor crónico:** Un brote de BVD, IBR, o una entrada de animales con brucelosis puede significar la pérdida de miles de cabezas y una clausura operativa. El ingreso de animales de múltiples orígenes (distintos criadores, distintas provincias) hace que el control sanitario al ingreso sea crítico y complejo.
* **Falta de historial:** Los terneros llegan sin información confiable de su historia sanitaria previa. El feedlot asume el riesgo a ciegas.
* **Gestión de medicamentos:** El control de stock de vacunas, antibióticos y antiparasitarios, con sus lotes, vencimientos y dosis aplicadas por animal, se hace mayoritariamente en planillas Excel o cuadernos.
* **Nueva presión regulatoria:** La Resolución SENASA 841/2025 y las restricciones a antimicrobianos elevan exigencias de registro sin proveer herramientas digitales para cumplirlas. Ver [[Barreras_Sanitarias_Antimicrobianos]].

### 2. Nutrición y Conversión: el KPI que Definen la Rentabilidad
* **El costo de la ración:** El feedlot compra maíz, expeller de soja, silaje y balanceados. Cualquier variación de precio impacta directamente en el margen neto. El cálculo de conversión (kg de alimento / kg de carne producida) es el indicador más crítico del negocio.
* **Formulación artesanal:** La mayoría de los feedlots medianos formulan la ración con el veterinario o nutricionista de forma periódica (quincenal o mensual), sin ajuste dinámico basado en datos de consumo real por lote.
* **Desperdicio y robo:** El control de la ración distribuida por mixer vs. la consumida por lote es manual y propenso a errores. El desperdicio de alimento es un costo silencioso enorme.

### 3. Trazabilidad y DT-e: Obligatorio pero Doloroso
* **El documento de tránsito electrónico (DT-e):** Desde su implementación masiva, el feedlot debe gestionar DT-e tanto al ingreso como al egreso de animales. La gestión manual o con sistemas fragmentados genera errores de RENSPA, inconsistencias con SENASA y retenciones en el frigorífico.
* **Conciliación imposible:** Un feedlot que recibe 500 terneros de 20 productores distintos en una semana tiene 20 DT-e de ingreso, cada uno con sus propias inconsistencias. Conciliar esto contra el sistema SIGSA de SENASA es una pesadilla operativa.
* **Egresos parciales:** La venta al frigorífico se hace en remesas parciales (100-200 animales por viaje). Cada egreso requiere un DT-e nuevo, con los animales seleccionados por peso, categoría y destino. Ver [[Pain Points de Trazabilidad]].

### 4. Control de Inventario y Mortandad
* **El "pozo negro" del inventario:** La diferencia entre animales ingresados, muertos, vendidos y existentes actuales raramente cuadra en tiempo real. La mortandad tiene que ser registrada ante SENASA pero muchos feedlots la informan con retraso o estimación.
* **Kilos perdidos sin causa:** No identificar tempranamente animales enfermos o con bajo consumo dentro de una tropa de 1.000 cabezas se traduce en kilos de carne que nunca se producen.

### 5. Financiamiento y Exposición al Precio
* **Capital inmovilizado:** El feedlot compra el ternero hoy (a precio de mercado) y lo vende en 4 meses. Durante ese período tiene capital inmovilizado altamente expuesto a variaciones del precio del gordo y del precio de la ración.
* **Sin cobertura eficiente:** El mercado de futuros ganaderos en Argentina es muy poco líquido. La mayoría de los feedlots opera "a precio abierto", absorbiendo toda la volatilidad.

## Sinergias Laterales P2P

### 1. Pools de Compra de Insumos
Los feedlots medianos se agrupan informalmente para comprar maíz en conjunto a acopiadores, logrando descuentos por volumen. Esta coordinación ocurre mayormente por WhatsApp y sin soporte de plataforma.

### 2. Intercambio de Información Sanitaria Regional
Cuando aparece un brote (ej. Queratoconjuntivitis, Complejo Respiratorio Bovino) en un feedlot de la zona, la alerta se pasa informalmente entre operadores de la región para anticipar el riesgo. No existe plataforma formal de alertas sanitarias feedlot-to-feedlot.

## Fuentes y Vínculos (Wiki)

* Conceptos relacionados: [[Pain Points de Trazabilidad]], [[Barreras_Sanitarias_Antimicrobianos]], [[Aumento de Densidad en Feedlots]], [[DT-e]], [[Incertidumbre Regulatoria Sanitaria]].
* Entidades relacionadas: [[Frigorifico Gorina]], [[Consorcio de Frigorificos ABC]], [[Contratista Rural]].
* Oportunidades relacionadas: [[MEVA_Verification_SaaS]], [[Full_Stack_Traceability_Hub]], [[Chemical_Compliance_SaaS]].
* Regulaciones: [[Resolucion SENASA 841-2025]].
