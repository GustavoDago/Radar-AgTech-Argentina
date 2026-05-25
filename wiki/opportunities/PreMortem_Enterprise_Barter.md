---
type: pre_mortem
opportunity: [[Enterprise_Barter_Engine]]
high_leverage: yes
tech_stack: [Java/Quarkus/Axon]
date: 2026-05-25
verdict: REQUIERE REDISEÑO FUNDAMENTAL
---

# Pre-Mortem: Enterprise Barter Engine (Autopsia Prospectiva)

**Documento de Análisis de Riesgo Crítico y Fortificación de Arquitectura**  
*Facilitador Estratégico Senior & AgTech VC*

---

## FASE 0 — RADIOGRAFÍA PREVIA

### 1. Tesis Central
Automatizar el clearing del canje de granos en Argentina mediante un motor de conciliación transaccional (Quarkus/Axon) conectado a APIs estatales (ARCA) e intermediarios financieros (Matba Rofex) para acelerar la liquidación de insumos y eliminar el riesgo cambiario de cooperativas y distribuidores.

### 2. Vectores de Fricción SFaaS Activados
*   **Vector 1: Integración Técnica (Integration-as-a-Service):** Dependencia crítica y en tiempo real de los servicios web de ARCA (CPE y LPG), APIs de BCR Labs y WebSockets de Matba Rofex.
*   **Vector 4: Asimetría Algorítmica:** Implementación de motores de reglas (Drools) para emular la cambiante e impredecible normativa fiscal de retenciones de IVA/Ganancias de ARCA.
*   **Vector 6: Desacople Físico-Digital:** Conciliación automatizada entre eventos digitales (CPE, cotizaciones financieras) y la realidad física del pesaje de camiones en balanzas de acopio remotas (IoT).

### 3. Vectores Ignorados (Puntos Ciegos)
*   **Vector 2: Mutualización (Private Pooling):** El plan asume que la infraestructura física de pesaje, conectividad y conectividad de balanzas de las cooperativas agrícolas funciona de forma aislada sin necesidad de consorciar el costo o mantenimiento ante el abandono del Estado.
*   **Vector 5: Desprotección Geopolítica (EUDR & Exportación):** Ignora por completo que los granos liquidados en canje a menudo tienen destino de exportación. Al no capturar la segregación física por compliance ambiental (EUDR/trazabilidad de deforestación) desde el origen del canje, el motor procesa granos fungibles que las cerealeras rechazarán en el Up-River.

### 4. Supuestos Ocultos
1.  **Estabilidad transaccional de APIs estatales:** Se asume que los servicios web de ARCA (ex-AFIP) para la emisión/validación de LPG y CPE son APIs de baja latencia y alta disponibilidad capaces de tolerar un flujo transaccional continuo bajo una arquitectura orientada a eventos (Axon) sin bloqueos del token de autenticación.
2.  **Invariabilidad y simetría de pesajes físicos:** Se asume que las balanzas de acopio (IoT) reportan datos limpios y calibrados de forma automática, ignorando las tolerancias físicas de merma, humedad, discrepancias entre balanza de origen y destino, y la manipulación manual de datos por parte de los operadores de planta.
3.  **Delegación de Hedging Algorítmico Incondicional:** Se asume que el CFO de una cooperativa o distribuidora de insumos delegará la ejecución de futuros de Matba Rofex (cobertura cambiaria de millones de dólares) a un WebSocket y un trigger automático basado en un evento de pesaje físico sin intervención ni validación humana.

### 5. Modelo B2B/B2C Check
*   **Target:** Cooperativas Agrícolas, Distribuidores de Insumos, Corredores de Granos.
*   **Monetización:** Cobro de suscripción SaaS en USD o canje físico indexado a USD de grandes cuentas corporativas.
*   **Veredicto de Viabilidad de Cliente:** **Aprobado**. El perfil del cliente cuenta con alta capacidad de pago en base dólar/grano y sufre una pérdida real de capital por la demora administrativa del canje.

---

## FASE 1 — EL ESCENARIO CATASTRÓFICO (Noviembre 2027: T+18 Meses)

Es **25 de Noviembre de 2027**. Enterprise Barter Engine ha fracasado estrepitosamente. La empresa se encuentra en cese de operaciones, con un Churn acumulado del 100% en los 12 clientes piloto medianos y grandes que habían integrado la solución en la Zona Núcleo. 

Las pérdidas de capital superan los USD 2.5 millones de financiamiento inicial y la reputación de la firma de software está destruida tras provocar incidentes graves de descalce financiero y sanciones de fiscalización tributaria de ARCA a tres de las cooperativas más grandes de Santa Fe. Los ERPs corporativos (SAP y Finnegans) han sido desconectados de nuestras APIs y los servidores de Axon en AWS han sido apagados. 

El propósito de este comité forense no es rescatar el plan; es realizar una autopsia forense para descubrir la cadena causal exacta del colapso.

---

## FASE 2 — PANEL DE FORENSES

Para realizar el análisis del colapso, se ha constituido un panel ciego de 5 especialistas de la realidad AgTech argentina:

1.  **Dr. Conrado Zavalía (El Regulador Fantasma):** Ex-asesor de la AFIP/ARCA, especialista en derecho tributario y administrativo agrícola en Argentina. *Justificación:* Evaluará cómo la volatilidad de las normativas de ARCA y los cambios en las reglas impositivas dinámicas volvieron insostenible el motor de reglas Drools.
2.  **Ing. Agr. Mateo "El Gringo" Rostagno (El Operador de Trinchera):** Gerente de Operaciones de una mega-cooperativa de acopio en San Justo (Santa Fe). *Justificación:* Evaluará el barro de la realidad física, los cortes de conectividad rural, las mermas por humedad y las discrepancias físicas que el sistema digital pretendía omitir.
3.  **María Sol de las Carreras (El Escéptico Financiero):** VC Partner especializada en Fintech/Agtech Latam. *Justificación:* Desmenuzará el descalce financiero provocado por el hedging algorítmico ciego y el verdadero costo de venta (CAC) de un sistema crítico que requería integraciones ad-hoc con ERPs obsoletos.
4.  **Dr. Esteban Spinetto (El Ingeniero de Sistemas):** Arquitecto de Software transaccional de alta concurrencia. *Justificación:* Expondrá cómo la inestabilidad de las APIs de ARCA y el cuello de botella del Event Store de Axon provocaron una desincronización letal del estado de las liquidaciones impositivas.
5.  **Dra. Valeria Rostán (El Geopolítico Frío):** Directora de Cumplimiento de Exportación de una de las "ABCD" grain traders en Rosario. *Justificación:* Explicará cómo la omisión de la trazabilidad EUDR en el canje impidió la descarga física de granos en los puertos del Up-River, bloqueando el clearing de punta a punta.

---

## FASE 3 — HISTORIAS DEL DESASTRE FORENSE

### 1. El Regulador Fantasma (Dr. Conrado Zavalía)
*   **El Detalle Fatal Ignorado:** La falsa creencia de que las reglas fiscales de ARCA para canje (como el cálculo de retenciones del IVA y Ganancias con regímenes especiales como el SISA - Sistema de Información Simplificado Agrícola) se pueden estructurar de forma estática en un motor de reglas empresariales (Drools).
*   **La Cadena Causal:** En el mes 3, ARCA modificó dinámicamente las alícuotas del SISA basadas en scoring de cumplimiento que cambiaba diariamente para cada CUIT de productor. En el mes 6, un parche fiscal de emergencia de ARCA cambió el formato de los XMLs para la emisión de la Liquidación Primaria de Granos (LPG). Nuestro motor Drools no pudo actualizarse a la velocidad del boletín oficial. El sistema procesó miles de liquidaciones calculando mal las retenciones. En el mes 12, los clientes recibieron notificaciones de exclusión del régimen SISA y multas de ARCA debido a las discrepancias. La plataforma se convirtió en una trampa fiscal.
*   **El Veredicto del Vector:** **Vector 4 (Asimetría Algorítmica)**. Intentamos encapsular como determinista un sistema fiscal estatal que opera como una caja negra de castigo ex-post.

### 2. El Operador de Trinchera (Ing. Mateo "El Gringo" Rostagno)
*   **El Detalle Fatal Ignorado:** El supuesto de que el peso reportado por la balanza IoT del acopio es un dato limpio, inmediato y definitivo para gatillar transacciones financieras.
*   **La Cadena Causal:** En el mes 4, la fibra óptica de la cooperativa en el interior de Córdoba sufrió un corte de 48 horas. Las balanzas continuaron despachando camiones en papel. El sistema digital se desincronizó. Peor aún: el sistema no toleraba el "barro operativo". Los camiones ingresaban con 4% de humedad de grano y 1.5% de residuo (tierra/chaucha de soja). El motor procesaba el peso bruto en tiempo real para disparar el hedging en Matba Rofex. Sin embargo, tras el análisis físico de laboratorio de calidad (24 horas después), la merma neta redujo el volumen en toneladas. La cooperativa terminó sobre-cubierta en el mercado de futuros de forma constante, asumiendo pérdidas millonarias por diferencias físicas no contempladas por el clearing algorítmico.
*   **El Veredicto del Vector:** **Vector 6 (Desacople Físico-Digital)**. El motor falló por un desprecio absoluto hacia la física del grano y la realidad del transporte rural.

### 3. El Escéptico Financiero (María Sol de las Carreras)
*   **El Detalle Fatal Ignorado:** El riesgo cambiario y operativo de ejecutar coberturas (hedging) automatizadas de futuros de Matba Rofex sin un colchón de liquidez (margin call safety pool) y con integraciones manuales en los ERPs de destino.
*   **La Cadena Causal:** En el mes 9, en medio de una corrida cambiaria y volatilidad extrema del dólar MEP, el sistema gatilló de forma automatizada órdenes de venta de futuros en Matba Rofex durante un pico de descarga física en el acopio. Debido a un retraso de 3 minutos en el WebSocket de cotizaciones, las órdenes se ejecutaron a precios desactualizados. Simultáneamente, el ERP (SAP) de la distribuidora de insumos rechazó la inyección de los asientos debido a un bloqueo por cierre de mes contable. La cooperativa quedó expuesta sin cobertura real y con órdenes ejecutadas en el mercado que requirieron garantías líquidas en pesos que no tenían presupuestadas, forzando la venta de stock físico a pérdida para cubrir los margin calls del bróker. El CAC del sistema se volvió insostenible frente a la personalización requerida por cada ERP legacy.
*   **El Veredicto del Vector:** **Vector 1 (Integración Técnica - Integración de Negocio)**. El "milisegundo de validación" fue una fantasía técnica que chocó contra los ciclos contables manuales y los cuellos de botella de liquidez del agro.

### 4. El Ingeniero de Sistemas (Dr. Esteban Spinetto)
*   **El Detalle Fatal Ignorado:** El uso de una arquitectura de Event Sourcing con Axon Framework conectada de forma síncrona a APIs de terceros lentas y no transaccionales (los Web Services SOAP de ARCA).
*   **La Cadena Causal:** En el mes 5, durante el pico de la cosecha gruesa (mayo), el volumen de transacciones se multiplicó por 40. La API de ARCA para validar las CPE (Cartas de Porte Electrónicas) comenzó a tardar hasta 45 segundos por petición o directamente arrojaba errores 504. Nuestra arquitectura orientada a eventos mantuvo abiertas las transacciones esperando la respuesta síncrona del middleware estatal para persistir el evento en el Event Store de PostgreSQL. Esto generó un bloqueo total de los hilos del pool de Quarkus y un desborde de memoria. Las transacciones de clearing quedaron en un estado "limbo". Al intentar reconstruir el estado de la cuenta corriente de los productores mediante el replay de eventos, el sistema duplicó las deducciones de deudas de insumos. La inconsistencia de datos destruyó la confianza en el sistema contable en menos de 72 horas.
*   **El Veredicto del Vector:** **Vector 1 (Integración Técnica)**. La arquitectura de microservicios con Quarkus y Axon es brillante en laboratorios cerrados, pero es extremadamente frágil cuando se la acopla al backend inestable y no transaccional del Estado de Datos.

### 5. El Geopolítico Frío (Dra. Valeria Rostán)
*   **El Detalle Fatal Ignorado:** Creer que el clearing de canje de granos es un proceso puramente local y financiero, obviando la regulación europea de deforestación (EUDR) y los estándares internacionales de exportación.
*   **La Cadena Causal:** Para mediados de 2026, los grandes exportadores del Up-River (Cargill, Viterra, Bunge) empezaron a exigir que todo grano entregado contara con geolocalización de origen libre de deforestación para cumplir con la EUDR europea. Nuestro motor de canje automatizado conciliaba contratos e insumos a nivel financiero y de volumen genérico. En el mes 10, cuando las cooperativas intentaron descargar los granos del clearing automatizado en puerto, las cerealeras rechazaron las barcazas porque el sistema no había trazado las coordenadas geográficas de las parcelas específicas donde se cosechó ese canje. El grano "limpio" se mezcló físicamente con grano no trazado en los acopios debido a que el software no tenía segregación física algorítmica. El colapso del canje fue total porque las cooperativas se quedaron con grano que no podían liquidar al exportador.
*   **El Veredicto del Vector:** **Vector 5 (Desprotección Geopolítica)**. Ignorar que el destino final del subyacente del canje es la exportación global altamente regulada.

---

## FASE 4 — ANTÍDOTO TÁCTICO Y MAPA DE RIESGOS

### A. Los 3 Vectores de Riesgo Macro

| Vector de Riesgo | Probabilidad | Horizonte | Vector de Fricción SFaaS Comprometido | Justificación |
|---|---|---|---|---|
| **Colapso/Latencia extrema de APIs de ARCA en Cosecha Gruesa** | **Alta** | T+3 a T+6 meses | **Vector 1:** Integración Técnica | Las APIs fiscales del Estado argentino no están diseñadas para responder como endpoints de alta disponibilidad para automatizaciones en tiempo real. |
| **Discrepancia y Ajustes por Mermas Físicas (Humedad/Calidad)** | **Alta** | T+1 a T+2 meses | **Vector 6:** Desacople Físico-Digital | El peso inicial de balanza nunca equivale al peso neto impositivo y comercial tras el análisis de laboratorio de calidad (BCR Labs). |
| **Rechazo de Destino de Grano por Incumplimiento EUDR** | **Media-Alta** | T+6 a T+12 meses | **Vector 5:** Desprotección Geopolítica | La incapacidad de segregar geográficamente el grano en el momento de la liquidación del trueque rompe la cadena de custodia exigida por los exportadores. |

---

### B. Ajustes Arquitectónicos de Fortificación

1.  **Desacoplamiento Asíncrono de APIs Estatales (Queue & Outbox Pattern):**
    *   *Descripción:* Eliminar cualquier llamada bloqueante síncrona a ARCA dentro del flujo transaccional de Axon. Implementar un patrón Outbox con colas de mensajería (RabbitMQ/Kafka) con reintentos exponenciales y manejo de estado intermedio ("Liquidación en Proceso de Aprobación").
    *   *Costo/Tiempo:* 4 semanas de desarrollo senior / Medio.
    *   *Mitigación:* Evita la caída del clearing y el desborde de memoria en Quarkus cuando ARCA arroja errores 504 o latencias de segundos.
2.  **Cámara de Compensación Operativa (Buffer de Conciliación de Humedad y Calidad):**
    *   *Descripción:* Prohibir el hedging financiero en Matba Rofex basado en el peso bruto inicial de balanza. El motor debe operar con un "Peso Neto Estimado" aplicando un algoritmo de descuento por humedad y calidad histórico, y esperar el JSON definitivo de BCR Labs para emitir el trigger de clearing final.
    *   *Costo/Tiempo:* 3 semanas de modelado y desarrollo / Bajo-Medio.
    *   *Mitigación:* Elimina el riesgo de sobre-cobertura y pérdidas financieras por diferencias físicas entre la balanza física y la liquidación real.
3.  **Trazabilidad EUDR Nativa en el Canje (Módulo de Segregación de Lotes):**
    *   *Descripción:* Integrar al motor de clearing la validación de coordenadas de origen del polígono del lote (vía integración con plataformas de GIS o autodeclaración georreferenciada SISA) antes de permitir la firma digital del contrato de canje de insumos.
    *   *Costo/Tiempo:* 6 semanas de desarrollo / Alto.
    *   *Mitigación:* Asegura que el grano canjeado sea aceptado por los exportadores en puerto y no pierda su valor de mercado.
4.  **Circuit Breaker y Aprobación Humana en Hedging Financiero (Mesa de Dinero Híbrida):**
    *   *Descripción:* Implementar límites estrictos de variación cambiaria y volumen para la ejecución automática de futuros en Matba Rofex. Si el mercado sufre picos de volatilidad superiores a un umbral predefinido, o si el ERP no confirma la registración del asiento en 60 segundos, el sistema debe pausar el trigger financiero y requerir la aprobación manual del CFO mediante un Dashboard de Excepciones.
    *   *Costo/Tiempo:* 4 semanas / Medio.
    *   *Mitigación:* Evita descalces financieros catastróficos por fallas de conexión o variaciones violentas de mercado.
5.  **Motor de Reglas Impositivas Híbrido con Soporte Legal Continuo (Drools + Compliance Engine):**
    *   *Descripción:* Rediseñar el componente Drools para que no dependa únicamente de código duro. Crear una interfaz visual de configuración de retenciones editable por contadores tributaristas agrícolas dedicados a actualizar las alícuotas del SISA diariamente.
    *   *Costo/Tiempo:* 5 semanas / Alto.
    *   *Mitigación:* Permite adaptar el sistema a los parches normativos de ARCA de forma inmediata sin requerir un despliegue de código del equipo de ingeniería.

---

### C. VEREDICTO FINAL

⚠️ **REQUIERE REDISEÑO FUNDAMENTAL**

**Justificación Estratégica:**  
El Enterprise Barter Engine persigue una de las fricciones más reales y lucrativas de la agricultura argentina: la ineficiencia fiscal y administrativa del canje de granos. Sin embargo, su diseño actual sufre de un **optimismo de laboratorio extremo**. Asume que la física de la soja, las APIs del Estado y los mercados financieros pueden conectarse en un flujo transaccional en tiempo real, síncrono y completamente automatizado. 

Antes de inyectar capital o iniciar el desarrollo de la arquitectura Quarkus, el proyecto debe ser rediseñado para operar bajo la premisa de que **las APIs estatales fallarán de forma constante, la calidad física del grano alterará el volumen final horas más tarde, y los mercados requerirán trazabilidad internacional ambiental estricta (EUDR)**. Sin estos 5 ajustes de arquitectura defensiva, la solución colapsará en su primera campaña de cosecha gruesa.

---
*Fin del Reporte Forense.*
