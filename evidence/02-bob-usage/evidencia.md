# Evidencia — Uso de Bob

## Resumen de participación de Bob

Bob participó activamente en **todas las etapas** del SDLC. A continuación los prompts
clave documentados, con análisis de calidad y las decisiones técnicas que tomó.

---

## Prompts documentados

### 🔵 Prompt 1 — Planificación (modo `Plan`)

```
Eres un analista de software. A partir del siguiente requerimiento, genera:
1. Una lista de historias de usuario en formato "Como [rol], quiero [acción] para [beneficio]"
2. Los criterios de aceptación de cada historia
3. Las entidades de datos principales que necesitaremos

Requerimiento:
El Centro de Monitoreo Planetario necesita un sistema CLI en Python para rastrear NEOs
usando la NASA NeoWs API. Debe: consultar por rango de fechas (máx 7 días), ordenar por
tamaño o velocidad, identificar el de menor miss_distance, y mantener una watchlist en memoria.
```

**Análisis de calidad:** ✅ Prompt con rol definido ("analista de software"), formato de
salida especificado (3 ítems numerados), contexto técnico completo. Evita respuestas
genéricas al incluir el dominio específico.

**Decisión técnica:** Bob identificó que `miss_distance` vendría como string en el JSON
de NASA y recomendó conversión explícita a `float` — crítico para la comparación numérica.

---

### 🔵 Prompt 2 — Diseño (modo `Ask`)

```
Basándome en estas historias de usuario para NeoTracker en Python CLI:
[HU-1 a HU-6]

Propón:
1. Una arquitectura de módulos sin dependencias externas (solo stdlib)
2. Los comandos CLI a exponer
3. Un diagrama ASCII de la arquitectura
4. Cómo manejar el estado de la watchlist entre comandos CLI

Restricción: Python 3.9+, sin pip install de nada.
```

**Análisis de calidad:** ✅ Contexto rico (restricción técnica explícita), historial
previo referenciado, pregunta específica sobre el estado en memoria (punto no obvio).

**Decisión técnica:** Bob sugirió instancia global en `watchlist_service.py` para el
estado en memoria dentro de una sesión CLI. El equipo aprobó por simplicidad.

---

### 🔵 Prompt 3 — Desarrollo (modo `Agent`)

```
Actúa como desarrollador senior en Python 3.9+.
Crea la estructura del proyecto NeoTracker con estos módulos:
  models.py, nasa_client.py, analyzer.py, watchlist_service.py, cli.py

Requisitos técnicos:
- Solo stdlib (urllib, argparse, unittest, dataclasses)
- Consume GET https://api.nasa.gov/neo/rest/v1/feed?start_date=...&end_date=...&api_key=DEMO_KEY
- Implementa: fetch por rango (máx 7 días), sort por size/velocity, find_most_dangerous
  (menor miss_distance numérico, NO string), watchlist add/remove/list en memoria
- Interfaz: CLI con argparse
- miss_distance.kilometers viene como STRING en el JSON — convertir a float antes de comparar

Crea los archivos en src/.
```

**Análisis de calidad:** ✅ Prompt "gordo" que evita ciclos de preguntas de Bob. Incluye:
rol (`desarrollador senior`), lenguaje, versión, módulos esperados, endpoint exacto,
restricción crítica (`miss_distance` como string → float). Un solo prompt generó los 5 archivos.

**Decisión técnica:** Bob eligió `dataclasses` sobre dict para `NearEarthObject` —
más legible y con tipado explícito, sin necesidad de `pydantic`.

---

### 🔵 Prompt 4 — Corrección quirúrgica (modo `Agent`)

```
En src/analyzer.py, la función find_most_dangerous() usa min() con key=lambda.
Verifica que miss_distance_km se esté comparando como float y no como string.
Solo modifica esa función si hay un bug — no toques nada más.
```

**Análisis de calidad:** ✅ Prompt quirúrgico: identifica el archivo, la función, el
problema exacto y explícitamente prohíbe cambios innecesarios.

---

### 🔵 Prompt 5 — Tests (modo `Agent`)

```
Genera pruebas unitarias para NeoTracker en src/.
Usa datos mock (sin llamadas reales a la NASA API).
Cubre exactamente estos casos:
1. sort_by_velocity ascendente
2. sort_by_size descendente
3. find_most_dangerous (menor miss_distance)
4. WatchList.add() — agregar un NEO
5. WatchList.add() duplicado — debe retornar False y no agregar
6. WatchList.remove() — eliminar existente

Framework: unittest (stdlib). Guarda en tests/test_neotracker.py.
Incluye fixture con 5 NEOs mock con valores distintos de tamaño, velocidad y distancia.
```

**Análisis de calidad:** ✅ Los 6 casos especificados explícitamente, datos mock pedidos
desde el prompt, framework definido, ubicación del archivo especificada.

**Resultado:** 17 tests generados (Bob agregó casos borde como lista vacía y comparación
numérica), todos pasando.

---

### 🔵 Prompt 6 — Documentación (modo `Agent`)

```
Genera un README-solution.md completo para el proyecto NeoTracker que ya existe en src/.
Léelo primero antes de escribir. Debe incluir:
1. Descripción del sistema
2. Tecnologías usadas
3. Instalación y ejecución (Python stdlib, sin pip)
4. Cómo obtener API key gratuita de NASA
5. Ejemplos reales de los 3 subcomandos: fetch, danger, watch
6. Estructura del proyecto
7. Cómo correr los tests
8. Diagrama ASCII de arquitectura

Guárdalo como README-solution.md en la raíz.
```

**Análisis de calidad:** ✅ Instruye a Bob a leer el código antes de escribir (evita
inconsistencias), 8 secciones especificadas, formato de salida definido.

---

## Bob en decisiones técnicas (no solo código)

| Decisión | Participación de Bob |
|----------|----------------------|
| Arquitectura de módulos | Bob propuso la separación por responsabilidad |
| `miss_distance` como string | Bob advirtió la conversión necesaria |
| Usar `dataclasses` para `NearEarthObject` | Bob eligió sobre dict |
| Instancia global para watchlist | Bob sugirió el patrón para CLI |
| 17 tests en lugar de 6 | Bob agregó casos borde no pedidos explícitamente |
| Solo stdlib | Bob respetó la restricción y adaptó la arquitectura |
