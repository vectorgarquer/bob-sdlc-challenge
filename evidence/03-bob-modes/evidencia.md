# Evidencia — Modos de Bob

## Resumen de uso de modos

| Etapa | Modo usado | Justificación |
|-------|-----------|---------------|
| Planificación | `Plan` | Solo razonamiento — sin tocar archivos ni ejecutar comandos |
| Diseño | `Ask` | Consulta técnica sobre arquitectura — sin modificar el proyecto |
| Desarrollo | `Agent` | Necesita crear archivos, leer el proyecto, ejecutar comandos |
| Pruebas | `Agent` | Crea el archivo de tests y puede ejecutarlos |
| Documentación | `Agent` | Lee el código existente antes de escribir el README |
| Entrega | `Agent` | Ejecuta git add, commit, push |

---

## Detalle por modo

### 🟣 Modo `Plan` — Etapa de Planificación

**Cuándo se usó:** Al inicio del challenge, antes de tocar cualquier archivo.

**Por qué `Plan` y no `Agent`:**
- En `Plan`, Bob no ejecuta herramientas (no lee archivos, no hace llamadas).
- Esto lo hace significativamente más eficiente en tokens para discusión conceptual.
- Permite pensar en voz alta con Bob sin que empiece a escribir código prematuramente.
- Ideal para generar historias de usuario, criterios de aceptación y entidades de datos.

**Resultado concreto:** 6 historias de usuario con criterios de aceptación + entidades
`NearEarthObject` y `WatchList` identificadas.

---

### 🔵 Modo `Ask` — Etapa de Diseño

**Cuándo se usó:** Para definir la arquitectura, los módulos y el contrato de la API
de NASA antes de escribir código.

**Por qué `Ask` y no `Plan`:**
- En `Ask`, Bob puede hacer búsquedas y responder preguntas técnicas concretas.
- Útil para preguntar sobre la estructura del JSON de la NASA NeoWs API.
- No modifica archivos, por lo que es seguro para explorar opciones de arquitectura.

**Por qué `Ask` y no `Agent`:**
- En esta etapa no se necesita crear archivos aún.
- `Ask` consume menos tokens que `Agent` porque no activa herramientas de exploración.

**Resultado concreto:** Arquitectura de 5 módulos definida, diagrama ASCII de flujo,
decisión de usar solo stdlib documentada.

---

### 🟢 Modo `Agent` — Desarrollo, Tests y Documentación

**Cuándo se usó:** Desde el momento en que hubo que crear archivos hasta el PR final.

**Por qué `Agent` y no `Ask`:**
- `Agent` tiene acceso a herramientas: crea archivos, lee el proyecto, ejecuta comandos.
- Puede crear los 5 archivos de `src/` en una sola interacción.
- Puede leer el código existente antes de generar los tests — evita inconsistencias.
- Puede ejecutar los tests y reportar el resultado directamente.

**Uso en desarrollo:** Un solo prompt "gordo" generó los 5 archivos de `src/` con código
funcional y correcto.

**Uso en tests:** Bob leyó `src/models.py` y `src/analyzer.py` antes de escribir los
tests — los fixtures de datos mock fueron consistentes con las clases reales.

**Uso en documentación:** Bob leyó todos los archivos de `src/` antes de generar el
`README-solution.md` — los ejemplos de comandos son correctos y los módulos listados
existen realmente.

---

## Lección aprendida sobre modos

> **La elección del modo correcto es en sí misma una estrategia de tokens.**
>
> Usar `Agent` para planificación habría hecho que Bob intentara leer archivos que
> aún no existen, desperdiciando tokens en herramientas fallidas.
> Usar `Plan` para desarrollo habría impedido que Bob creara archivos.
> Cada modo tiene su momento exacto.
