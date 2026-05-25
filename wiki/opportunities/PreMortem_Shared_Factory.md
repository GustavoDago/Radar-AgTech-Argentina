# Pre-Mortem: Shared-Factory Protocol (SFP)
> **Asunto:** Autopsia prospectiva del plan de Manufacturing-as-a-Service Lácteo (SFP).  
> **Fecha de Análisis:** 2026-05-25  
> **Status:** Generado bajo la Directiva de Gobernanza (Tech Leader & Skeptic Mode).  
> **Referencia:** [[Shared_Factory_Protocol]]

---

## FASE 0: Radiografía previa

- **Tesis central:** Habilitar un modelo de "Manufacturing-as-a-Service Lácteo" (MaaS) donde múltiples mega-tambos e industrias ociosas alquilen y orquesten slots de procesamiento industrial a través de un protocolo de software que garantice la identidad y segregación de calidad en origen para exportación premium.
- **Vectores de Fricción activados:**
  - **Mutualización (Private Pooling):** Cooperativas y tambos compartiendo y co-financiando la utilización de infraestructura industrial de secado y procesamiento (fábricas paradas o subocupadas de Sancor/Verónica).
  - **Arbitraje y Confianza (Arbitration-as-a-Service):** Garantizar la segregación de calidad (grasa, proteína, rastros de antibióticos) e identidad preservada del lote lácteo sin intervención de un inspector estatal neutral continuo.
  - **Integración Técnica (Integration-as-a-Service):** Orquestar la logística de recolección y la capacidad de producción acoplando el protocolo con los ERPs industriales de terceros y las APIs de ARCA/SENASA.
- **Vectores ignorados:**
  - **Desacople Físico-Digital:** El plan asume una precisión algorítmica de slots de producción que ignora las restricciones de logística física en caminos de tierra intransitables de Santa Fe/Córdoba, el retardo térmico en la conservación de leche y el mantenimiento del circuito frío.
  - **Asimetría Algorítmica:** La imprevisibilidad de las normativas de ARCA y SENASA sobre el tránsito y facturación de la leche (Remito Electrónico Lácteo - REL), que actúan como bloqueos preventivos ex-post del transporte.
  - **Desprotección Geopolítica (EUDR & Exportación):** La presunción de que el comprador premium en la Unión Europea o Asia aceptará trazabilidad "blockchain-light" autodeclarada en lugar de certificaciones estatales oficiales.
- **Supuestos ocultos:**
  1. *El Dueño Colaborativo:* Se asume que los dueños de plantas ociosas cederán el control operativo de sus líneas y sistemas SCADA de manera neutral, sin priorizar su propia producción láctea o la de sus clientes históricos en los momentos críticos de parición (picos de primavera).
  2. *Inocuidad Estática:* Se asume que la segregación de calidad es controlable lógicamente a través de software, ignorando que las mezclas y contaminaciones cruzadas en tuberías compartidas ocurren a nivel mecánico y operativo físico-químico.
  3. *Inmunidad Sindical:* Se asume que el sindicato de la industria láctea (ATILRA) aceptará sin conflicto un esquema MaaS flexible que "uberiza" las jornadas y turnos de los operarios de planta según el flujo de slots reservados dinámicamente.
- **Modelo B2B o B2C check:** **B2B puro.** Los clientes y proveedores son grandes tambos (Mega-tambos), Pymes lácteas y plantas industriales. Las transacciones se cotizan sobre base USD o canje de leche en polvo / insumos dolarizados. No obstante, la exposición al riesgo del ecosistema cooperativo argentino (en pesos devaluados y con severa falta de liquidez) es alta.

---

## FASE 1: El escenario catastrófico (Noviembre de 2027)

Es noviembre de 2027. Dieciocho meses después del lanzamiento de SFP, **el protocolo ha colapsado de forma absoluta**. La tasa de churn de los mega-tambos adheridos es del 100%, las pérdidas acumuladas por obsolescencia y desperdicio físico de materia prima ascienden a 3.2 millones de dólares, y dos de las tres plantas piloto en Santa Fe y Córdoba han sido clausuradas por SENASA. Los inversores de Venture Capital han cancelado la línea de financiamiento Serie A y la compañía está en concurso de acreedores debido a demandas cruzadas por contaminación sanitaria y litigios laborales masivos de ATILRA. El software ha sido apagado; el "servidor de procesamiento de proteína" demostró ser una fantasía de Powerpoint.

---

## FASE 2: Panel de forenses

El panel de autopsia opera en aislamiento ciego para evitar el pensamiento grupal y devaluar el optimismo original del equipo técnico:

1. **El Regulador Fantasma (Dr. Ignacio "Nacho" Gorostiaga):** Especialista en Derecho Administrativo y Normativas Lácteas (ex-SENASA/ARCA). Su enfoque se centra en cómo las reglamentaciones de maquila láctea y la fiscalización del Remito Electrónico Lácteo (REL) destruyeron la flexibilidad legal del protocolo.
2. **El Operador de Trinchera (Bautista "Gringo" Cagnolo):** Administrador del mega-tambo "El Milagro" (8,500 vacas en ordeñe en Rafaela, Santa Fe). Analiza la inviabilidad logística, el lodo de la Zona Núcleo y el conflicto de campo con el personal técnico y los choferes de camiones cisterna.
3. **El Escéptico Financiero (Martina Rossi):** Partner en Pampa Ventures. Desmenuza los unit economics, el flujo de caja estrangulado por la brecha cambiaria, la cadena de cobro láctea y los costos de mermas físicas no calculadas en la simulación lógica.
4. **El Ingeniero de Sistemas (Ing. Marcos Funes):** Arquitecto Backend y especialista en Automatización Industrial (SCADA/PLCs). Explica el colapso del sistema lógico de identidad preservada al chocar con hardware heredado y el flujo físico de fluidos.
5. **El Geopolítico Frío (Dieter Kanzler):** ex-Director de Trazabilidad Láctea de un exportador global multinacional. Destroza el supuesto de que el protocolo digital de SFP servía como moat técnico para la exportación de alta gama a la UE.

---

## FASE 3: Historias del desastre forense

### 1. El Regulador Fantasma: El Laberinto Legal de la Maquila Sanitaria
- **El Detalle Fatal Ignorado:** La presunción de que el tránsito de leche cruda "multipropietario" y su procesamiento tercerizado en slots dinámicos se encuadraban fácilmente en la figura jurídica de la "maquila". Se ignoró que ARCA y SENASA exigen que el emisor de la materia prima, el procesador físico y el destinatario del producto terminado tengan un flujo documental rígido y no-estocástico (REL y DT-e nominados por lote específico previo al despacho).
- **La Cadena Causal:**
  - *Mes 2:* Se lanza la plataforma piloto. El software asigna dinámicamente leche del Tambo A a la Planta B. Sin embargo, las APIs de ARCA exigen que el Remito Electrónico Lácteo (REL) valide que el destinatario sea el titular de la planta o un operador comercial registrado con cupo fiscal lácteo vigente.
  - *Mes 5:* La velocidad algorítmica de SFP choca con el sistema fiscal. La plataforma "consolida" cargas de tres tambos distintos en un solo camión cisterna compartimentado para optimizar costos de flete. ARCA bloquea las cartas de porte por inconsistencia de origen-destino.
  - *Mes 9:* SENASA intercepta dos camiones con 60,000 litros de leche bajo sospecha de "tránsito clandestino" debido a que los DT-e del protocolo no coincidían con los destinos físicos reales reprogramados dinámicamente en tránsito. Toda la carga de leche premium se acidifica y decomisa.
  - *Mes 14:* Una inspección de ARCA determina que el modelo de cobro de slots MaaS encubre una intermediación comercial no autorizada, imponiendo multas del 150% de la facturación y suspendiendo el CUIT lácteo de los tambos intervinientes.
- **El Veredicto del Vector:** **Integración Técnica (Integration-as-a-Service) activado de forma defectuosa.** Las APIs del Estado no están diseñadas para la elasticidad de slots de Uber; exigir flujos rígidos a un backend flexible genera parálisis fiscal y clausuras.

### 2. El Operador de Trinchera: El Factor ATILRA y la Realidad del Lodo
- **El Detalle Fatal Ignorado:** El supuesto de que el personal de la planta industrial procesaría el "slot alquilado" con el mismo esmero y flexibilidad temporal que si fuera propio, ignorando la resistencia de ATILRA frente a cualquier software que busque eficientizar y flexibilizar los turnos de trabajo.
- **La Cadena Causal:**
  - *Mes 3:* El algoritmo de "Logística Inversa Dinámica" calcula un slot de procesamiento a las 02:00 AM para aprovechar tarifas eléctricas y disponibilidad de planta. Los delegados sindicales de ATILRA en la planta se niegan a arrancar la caldera fuera de la planificación del turno normal de la empresa, exigiendo pago de horas extras al 200%.
  - *Mes 6:* Para forzar la rentabilidad, SFP intenta reducir la ventana de lavado y desinfección (CIP - Clean In Place) mediante optimizaciones algorítmicas de secuencias de secado. El personal de planta inicia un paro de brazos caídos acusando "presión laboral desmedida" y violación del convenio colectivo.
  - *Mes 10:* Un temporal en la Zona Núcleo corta la conectividad en Rafaela durante 48 horas. El "Yield Orchestration Engine" no puede recibir datos de ordeñe. Los camiones cisternas se quedan sin ruteo dinámico y quedan varados en caminos de tierra intransitables. La leche premium decae en calidad bacteriológica antes de llegar a la planta.
  - *Mes 15:* Tras paros repetidos y camiones lecheros volcados en la banquina, los mega-tambos vuelven al esquema de entrega clásico a Mastellone para asegurar la descarga física, abandonando SFP.
- **El Veredicto del Vector:** **Desacople Físico-Digital ignorado de forma letal.** Las dinámicas de la infraestructura vial de tierra y la inercia sindical de ATILRA no se resuelven con un backend event-driven; el barro y las asambleas gremiales no consumen APIs.

### 3. El Escéptico Financiero: La Trampa de las Mermas Físicas e Inflación de Infraestructura
- **El Detalle Fatal Ignorado:** Ignorar la existencia del "Volumen Muerto" (Dead Volume) y las mermas mecánicas de proceso. Se asumió que si un tambo inyectaba 10,000 litros de grasa/proteína teórica al inicio del sistema de cañerías de una planta de secado, el motor lógico podría recuperar exactamente el 100% de la identidad preservada al final de la línea.
- **La Cadena Causal:**
  - *Mes 4:* El motor lógico en Java/Quarkus calcula un rendimiento teórico de Leche en Polvo Premium basado en los análisis del tambo. Sin embargo, en el paso físico por las cañerías del secador, un 4% de la proteína queda adherida a las paredes térmicas del atomizador (mermas industriales no computadas).
  - *Mes 7:* Los tambos exigen explicaciones por la diferencia física entre lo "facturado digitalmente" por el protocolo y los kilogramos reales de leche en polvo depositados en los big bags de exportación. Las pérdidas físicas de mermas superan el fee de SFP.
  - *Mes 11:* La brecha cambiaria y la devaluación del peso licúan la caja del protocolo. El costo operativo de los servidores en AWS (donde corre el motor lógico) y las integraciones está dolarizado, mientras que el cobro a los tambos está atado al precio de la leche de referencia SIGLeA (en pesos argentinos devaluados a 60 días).
  - *Mes 16:* Sin capital de trabajo para cubrir las mermas físicas no imputadas y con costos operativos en dólares disparados, la caja neta del protocolo se vuelve negativa de forma irreversible.
- **El Veredicto del Vector:** **Arbitraje y Confianza (Arbitration-as-a-Service) activado de forma defectuosa.** Un protocolo de software no puede arbitrar un balance de masas físico si no tiene control e instrumentación de las mermas reales del fierro industrial.

### 4. El Ingeniero de Sistemas: El Colapso de la Preservación de Identidad en Plantas Analógicas
- **El Detalle Fatal Ignorado:** La fe ciega en que las plantas lácteas obsoletas (Sancor/Verónica de los años 80/90) poseían la instrumentación, medidores de flujo Coriolis y automatización industrial (SCADA/PLCs modernos) necesarios para segregar de forma confiable lotes continuos de leche sin mezclarse en los tanques de recepción.
- **La Cadena Causal:**
  - *Mes 3:* Se implementa el backend en Quarkus. Al conectar los colectores de eventos al sistema SCADA de una planta del piloto, se descubre que la mayoría de las válvulas de derivación son manuales o mecánicas y no envían telemetría digital. El operario debe "abrir y cerrar a mano" las compuertas de los silos.
  - *Mes 8:* Por error de un operario mal entrenado que manipuló manualmente un colector para acelerar el vaciado de un tanque, un lote de 20,000 litros de leche con antibióticos del tambo "estándar" ingresó a la línea donde se procesaba la leche "orgánica certificada" del tambo premium.
  - *Mes 12:* La base de datos "Blockchain-Light" del SFP registraba digitalmente que el lote orgánico estaba perfectamente segregado y envasado en su correspondiente silo. Sin embargo, las pruebas químicas en laboratorio detectaron contaminación por antibióticos en todo el silo premium.
  - *Mes 16:* Se destruye la confianza técnica del protocolo. Los clientes premium exigen auditorías de hardware físico que SFP no puede proveer porque su capa de software no tiene sensores reales propios, dependiendo únicamente de declaraciones manuales en pantallas industriales obsoletas.
- **El Veredicto del Vector:** **Arbitraje y Confianza (Arbitration-as-a-Service) ignorado.** Creer que la inmutabilidad lógica digital en el backend compensa la anarquía física e instrumentación nula del hardware industrial es el error fundacional del software sin sensorización.

### 5. El Geopolítico Frío: El Veto Sanitario de los Mercados Premium
- **El Detalle Fatal Ignorado:** El supuesto de que el mercado de exportación de alta gama aceptaría un certificado "privado" basado en software sin una trazabilidad estatal física-veterinaria y sin el sello oficial in situ del SENASA que audite rigurosamente el proceso CIP (limpieza) entre lotes lácteos.
- **La Cadena Causal:**
  - *Mes 5:* SFP cierra su primer pre-contrato de exportación de Leche en Polvo Premium hacia un importador en Hamburgo (Alemania) bajo trazabilidad digital del protocolo.
  - *Mes 9:* El cargamento llega al puerto de Amberes. Las autoridades sanitarias europeas rechazan la documentación porque las normas oficiales de exportación láctea exigen que el certificado sanitario (monitoreado por SENASA en origen) valide la discontinuidad física total y lavado químico de 6 horas de las líneas de secado entre lotes premium y estándar.
  - *Mes 12:* SENASA se niega a firmar los certificados de exportación del protocolo MaaS debido a que los inspectores gubernamentales no pueden validar la inmutabilidad de la segregación lógica interna de SFP, al carecer de inspectores oficiales de campo destinados de forma continua a las plantas tercerizadas del pool.
  - *Mes 15:* Sin canal de exportación premium, la leche en polvo producida bajo SFP se tiene que malvender en el mercado interno argentino a precios regulados de subsistencia, destruyendo el margen económico del pool privado.
- **El Veredicto del Vector:** **Desprotección Geopolítica (EUDR & Exportación) ignorado por completo.** El comprador global no busca "blockchain" privada; busca compliance de soberanía sanitaria (SENASA validado oficialmente en destino). La tecnología sin la bendición reguladora estatal es inviable para exportar commodities con valor agregado.

---

## FASE 4: Antídoto táctico y mapa de riesgos

### A. Los 3 Vectores de Riesgo Macro

| Vector de Riesgo | Probabilidad | Horizonte Temporal | Vector de Fricción Comprometido | Justificación Técnica/Operativa |
| :--- | :--- | :--- | :--- | :--- |
| **Contaminación Física y Mermas no Deducidas** | **Alta** | Mes 1 a 3 | Arbitraje y Confianza / Desacople Físico-Digital | Las plantas carecen de control neumático automatizado y sensorización Coriolis; las mezclas mecánicas son inevitables. |
| **Parálisis Gremial (Factor ATILRA)** | **Alta** | Mes 3 a 6 | Mutualización / Desacople Físico-Digital | El modelo de slots de producción flexible rompe la planificación rígida del convenio colectivo del personal lácteo. |
| **Bloqueo Sanitario-Fiscal (SENASA/ARCA)** | **Media-Alta** | Mes 6 a 12 | Integración Técnica / Desprotección Geopolítica | La elasticidad comercial del protocolo no encaja con los sistemas inflexibles de emisión de REL, DT-e y trazabilidad exportadora oficial. |

---

### B. Ajustes Arquitectónicos Requeridos

Para soldar de manera proactiva al plan antes de cualquier inversión de capital o desarrollo de código:

#### 1. Sensorización Física Obligatoria en Planta (Edge Gateways)
- **Descripción:** No depender de la telemetría del SCADA de la planta. SFP debe instalar su propio set de sensores físicos portátiles no invasivos (sensores de flujo ultrasónicos y conductímetros ópticos para medir arrastre de sólidos y limpieza CIP) en las tuberías clave de entrada y salida del atomizador de secado.
- **Costo:** Medio ($45,000 USD por planta piloto / 4 semanas).
- **Riesgo Mitigado:** Contaminación cruzada indetectable por software y reclamos por mezcla física de leche premium y con antibióticos.

#### 2. Módulo Integrado de Gestión Fiscal Láctea (ARCA REL / SENASA SIGSA Engine)
- **Descripción:** Desarrollar en Quarkus un motor que pre-valide y emita de forma automatizada los Remitos Electrónicos Lácteos (REL) y DT-e antes de autorizar físicamente la salida del camión del tambo. Si la validación fiscal en ARCA falla o hay inconsistencia de CUITs, el algoritmo bloquea automáticamente la asignación de slots en tiempo real.
- **Costo:** Alto (3 meses de desarrollo de API e integraciones complejas).
- **Riesgo Mitigado:** Decomisos de leche premium por gendarmería/SENASA en ruta y bloqueos de cuenta fiscal de los tambos.

#### 3. Fideicomiso Lácteo y Pool de Garantía Láctea (Auditoría BCR Labs)
- **Descripción:** Constituir un fondo de cobertura en USD financiado con un porcentaje del fee de transacción de cada slot reservado. Adicionalmente, establecer a la Bolsa de Comercio de Rosario (BCR Labs) como auditor físico independiente encargado de tomar y validar las contra-muestras de leche en origen y destino antes del secado.
- **Costo:** Medio (Gastos legales y fee de laboratorio continuo).
- **Riesgo Mitigado:** Litigios judiciales cruzados por mermas y pérdida de identidad en origen.

#### 4. "Dead Volume Offset" en el Yield Engine
- **Descripción:** Modificar los algoritmos de cálculo de rendimiento teórico en Java incorporando un coeficiente de merma física dinámica y retención en cañería ajustable por planta (ej: 3% a 6% de "pérdida logística interna"). El software debe compensar esta pérdida asignando un slot mayor al productor para que el volumen neto final en big bags sea exacto.
- **Costo:** Bajo (2 semanas de refactorización matemática de backend).
- **Riesgo Mitigado:** Asimetría de balance de masas y denuncias por faltante de materia prima procesada.

#### 5. Contingencia Logística y Conectividad Robusta
- **Descripción:** Instalar terminales satelitales (Starlink) en las plantas del piloto y dotar a los camiones lecheros recolectores de dispositivos IoT de rastreo móvil que operen offline. Si se pierde la conectividad en la Zona Núcleo, el protocolo procesa el enrutamiento mediante un algoritmo offline de resiliencia local en el camión.
- **Costo:** Bajo-Medio ($15,000 USD equipamiento y abono anual).
- **Riesgo Mitigado:** Acidificación de materia prima por incomunicación en caminos rurales en época de tormentas.

---

### C. Veredicto Final

⚠️ **REQUIERE REDISEÑO FUNDAMENTAL**

**Justificación:** La tesis central de "Manufacturing-as-a-Service Lácteo" tiene un mérito conceptual innegable frente a la subocupación industrial en Argentina. Sin embargo, tal como está formulada en `Shared_Factory_Protocol.md`, es un plan excesivamente lógico e idealista. Pretender orquestar slots de proteínas en plantas lácteas argentinas obsoletas, altamente sindicalizadas por ATILRA y rigidizadas por regulaciones burocráticas estrictas (ARCA y SENASA) mediante un mero motor digital de asignación y una base de datos "blockchain-light" es una garantía de colapso físico y legal a los 18 meses. 

El proyecto **solo es viable** si se rediseña como una plataforma de control física-industrial que integre hardware propietario en las cañerías (sensores IoT de flujo/calidad) y un motor legal-fiscal que absorba el compliance nacional in situ, transformándolo de una solución meramente lógica a un protocolo operativo híbrido físico-digital con base legal blindada.
