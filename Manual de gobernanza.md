

## 1. Marco Filosófico y Objetivos Estratégicos

Nos encontramos ante un cambio de paradigma irreversible en la gestión del conocimiento corporativo. El modelo tradicional de Recuperación Aumentada por Generación (RAG) es inherentemente ineficiente: es un sistema "sin estado" que redescubre el conocimiento desde cero en cada consulta, fragmentando la información en procesos efímeros. Este manual dicta la transición hacia la **Wiki Compuesta (LLM Wiki)**, un ecosistema donde el conocimiento se acumula, se refina y se compila sistemáticamente.

Bajo este modelo, **"Obsidian es el IDE; el LLM es el programador; y la wiki es el código base"**. Esta arquitectura rescata la visión original de Vannevar Bush y su _Memex_ (1945): un almacén de conocimiento personal con "rastros asociativos" donde las conexiones entre documentos son tan valiosas como los documentos mismos. La pieza que Bush no pudo resolver —el mantenimiento— es ahora delegada íntegramente a agentes de IA.

Este documento no es solo una guía; es un **"Archivo de Ideas" (Idea File)**. Está diseñado para ser entregado a un agente de IA para que este instancie y gobierne el sistema de forma autónoma. Los objetivos estratégicos son:

- **Estandarización:** Estructura de archivos y metadatos predecible para una interoperabilidad total entre agentes.
- **Integridad:** Mantenimiento de una verdad única mediante procesos de "linting" que detectan contradicciones.
- **Trazabilidad Inmutable:** Registro auditable de cada síntesis y modificación mediante control de versiones.
- **Escalabilidad Exponencial:** Capacidad de gestionar miles de nodos sin degradación de la calidad ni aumento del coste operativo.

**El impacto estratégico:** Al delegar la autoría y el _bookkeeping_ al agente, reducimos el coste de la "deuda de conocimiento" a casi cero. El ser humano deja de ser un "tenedor de libros" para convertirse en un curador estratégico y formulador de preguntas complejas, permitiendo que el conocimiento genere un interés compuesto con cada interacción.

--------------------------------------------------------------------------------

## 2. Arquitectura Estándar de Tres Capas

La arquitectura de carpetas es el "sistema operativo" del repositorio. Para garantizar la estabilidad, dictamos una separación estricta de preocupaciones entre datos inmutables, síntesis generada y reglas operativas.

### Estructura del Repositorio

|   |   |   |   |
|---|---|---|---|
|Capa|Propietario|Permisos|Propósito|
|**Raw Sources** (`raw/`)|Humano|Lectura (IA)|Fuente de verdad inmutable (PDFs, artículos, imágenes).|
|**The Wiki** (`wiki/`)|Agente de IA|Lectura/Escritura|Espacio de síntesis: conceptos, entidades y comparaciones.|
|**The Schema** (Raíz)|Humano/IA|Lectura/Escritura|"Constitución" del sistema (`CLAUDE.md` / `AGENTS.md`).|

### Protocolo de Inmutabilidad y Estructura de Directorios

La capa `raw/` debe permanecer inalterada para permitir auditorías forenses. El agente tiene prohibido escribir en este directorio. Por el contrario, la capa `wiki/` es dominio exclusivo de la IA y debe estructurarse obligatoriamente en los siguientes subdirectorios:

- `wiki/sources/`: Resúmenes individuales de cada fuente en `raw/`.
- `wiki/concepts/`: Artículos sobre temas transversales (ej. "Mecanismos de Atención").
- `wiki/entities/`: Perfiles de organizaciones, personas o modelos específicos.
- `wiki/comparisons/`: Tablas y análisis comparativos derivados de consultas.

**¿Por qué Markdown sobre Bases de Datos Vectoriales?** A diferencia de las cajas negras vectoriales, el Markdown ofrece transparencia total. Permite la auditoría humana directa, es compatible con cualquier IDE (como Obsidian) y facilita el versionado mediante Git, asegurando que el conocimiento sea portátil y eterno.

--------------------------------------------------------------------------------

## 3. El Esquema de Configuración (CLAUDE.md / AGENTS.md)

El Esquema es la "Constitución" que transforma a un chatbot genérico en un mantenedor de conocimiento disciplinado. Su nombre de archivo dependerá del agente utilizado (`CLAUDE.md` para Claude Code, `AGENTS.md` para Codex/OpenCode).

### Ejemplo de Esquema Estándar

```markdown
### LLM Wiki Schema - Directiva de Gobernanza

#### Convenciones de Página (YAML Obligatorio)
---
type: [concepto | entidad | resumen | comparativa]
tags: [domain/tag]
sources: [links a archivos en raw/ o URLs]
confidence: [high | medium | low]
last_update: YYYY-MM-DD
---

#### Flujos de Trabajo
1. Ingest: Leer fuente en raw/ -> Extraer takeaways -> Crear/Actualizar wiki/sources/ -> Propagar cambios a conceptos/ y entidades/ -> Actualizar index.md y log.md.
2. Query: Consultar index.md -> Identificar páginas -> Sintetizar respuesta con citas [[wiki-links]] -> Ofrecer "Filing Back".
3. Lint: Detectar contradicciones, páginas huérfanas y gaps de información.
```

### Estándares de Metadatos

El uso de Frontmatter YAML es una exigencia técnica. Campos como `confidence` (nivel de confianza) y `sources` permiten que herramientas como **Dataview** generen cuadros de mando dinámicos, identificando áreas que requieren validación humana.

**Valor Estratégico:** El esquema asegura la "memoria persistente" entre sesiones. Sin él, el agente sufriría una degradación de estándares, perdiendo la coherencia estructural del repositorio.

--------------------------------------------------------------------------------

## 4. Protocolos de Operación: El Ciclo de Vida del Conocimiento

La gestión del wiki es una **compilación activa**. La ingesta de una sola fuente no es un evento aislado; es una actualización que debe propagarse por todo el grafo de conocimiento.

### Protocolo de Ingesta (El Efecto Ripple)

1. **Lectura:** Análisis de la fuente en `raw/`.
2. **Extracción y Compilación:** Creación del resumen en `wiki/sources/`.
3. **Propagación Dinámica:** Una sola ingesta debe actualizar entre 10 y 15 archivos relacionados (conceptos, entidades, índices).
4. **Indización:** Actualización del catálogo maestro `index.md` y registro en `log.md`.

### Protocolo de Consulta (Query) y "Filing Back"

Las consultas no son respuestas efímeras. Aplicamos la regla del **"Filing Back"**: cualquier síntesis valiosa generada para responder a una pregunta compleja debe convertirse en una página permanente en `wiki/comparisons/`. Así, las exploraciones del usuario se capitalizan como activos del repositorio.

### Protocolo de Salud (Linting)

El agente debe ejecutar periódicamente un "Lint de Conocimiento" para:

- **Detección de Contradicciones:** Identificar dónde la nueva evidencia choca con la síntesis anterior.
- **Identificación de Gaps:** Listar conceptos mencionados frecuentemente que aún no tienen una página propia.

**Eficiencia Operativa:** Mientras que un humano fallaría en mantener la consistencia al tocar 15 archivos tras una lectura, la IA realiza este _bookkeeping_ de forma instantánea, eliminando la fricción que suele destruir las wikis corporativas.

--------------------------------------------------------------------------------

## 5. Trazabilidad y Control de Cambios

En un entorno de autoría automatizada, la trazabilidad es la garantía de responsabilidad.

### Estándar de Log Cronológico (`log.md`)

El agente debe registrar cada movimiento en un formato parseable: `## [YYYY-MM-DD] operación | Título del documento/consulta` Esto permite entender la evolución del pensamiento del sistema y auditar las fuentes de cada cambio.

### Integración con Git: Supervisión Humana

El repositorio debe estar bajo control de versiones de **Git**. El uso de `git diff` y `git log` constituye la capa de supervisión humana definitiva. Permite validar exactamente qué líneas de texto ha alterado la IA, revertir "alucinaciones" estructurales y mantener un historial de evidencia infalible para la gobernanza empresarial.

--------------------------------------------------------------------------------

## 6. Ecosistema de Herramientas y Visualización

### El Stack Tecnológico

- **Obsidian:** El IDE del conocimiento.
- **qmd:** Motor de búsqueda local híbrido (BM25 para palabras clave + Vectorial para semántica + Re-ranking por LLM).
- **Marp:** Generación de presentaciones profesionales directamente desde el Markdown de la wiki.
- **Dataview:** Consultas SQL sobre el frontmatter YAML para detectar inconsistencias de datos.

### Protocolo de Persistencia de Imágenes

Para evitar enlaces rotos y garantizar la soberanía de los datos, dictamos el siguiente protocolo:

1. Configurar la ruta de archivos adjuntos en `raw/assets/`.
2. Uso obligatorio del hotkey **Ctrl+Shift+D** (Obsidian) para descargar imágenes locales tras el clipping de artículos.
3. **Workaround de Lectura:** El agente leerá primero el texto y luego, bajo demanda, procesará las imágenes locales para ganar contexto visual profundo.

**Visualización de Grafos:** El "Graph View" de Obsidian se utilizará como herramienta de diagnóstico para identificar silos de información y nodos críticos que requieran mayor investigación o conexión.

--------------------------------------------------------------------------------

## 7. Conclusión: El Futuro del Mantenimiento de Conocimiento Cero

Este marco de gobernanza marca el fin de la era del RAG estático y el comienzo del **conocimiento compuesto**. Al implementar esta Wiki, la organización deja de luchar contra la entropía de la información.

El valor de este sistema reside en su capacidad de **compilación incremental**. Cada fuente añadida y cada pregunta formulada no solo suma información, sino que multiplica las conexiones existentes. La labor humana evoluciona de la recopilación a la curación estratégica, apoyada en una memoria organizacional que nunca olvida y que reduce el coste de mantenimiento a niveles marginales. La co-evolución del esquema entre el humano y el agente es el nuevo estándar de oro de la inteligencia empresarial.