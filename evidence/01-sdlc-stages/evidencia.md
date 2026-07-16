# Evidencia — Etapas del SDLC

## Etapa 1 — Planificación (modo `Plan`)

**Prompt utilizado:**
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

**Historias de usuario generadas:**

| ID  | Historia | Criterios de aceptación |
|-----|----------|-------------------------|
| HU-1 | Como operador, quiero consultar NEOs en un rango de fechas para ver los asteroides próximos | - Rango máximo 7 días<br>- Retorna lista con nombre, tamaño, velocidad, distancia<br>- Error claro si el rango supera 7 días |
| HU-2 | Como operador, quiero ordenar la lista por tamaño estimado para identificar los más grandes | - Orden ascendente y descendente disponibles<br>- Usa diámetro promedio como criterio |
| HU-3 | Como operador, quiero ordenar la lista por velocidad relativa para priorizar los más rápidos | - Orden ascendente y descendente disponibles<br>- Usa km/h como unidad |
| HU-4 | Como operador, quiero identificar el asteroide con menor miss_distance para conocer el más peligroso | - Compara numéricamente (no como string)<br>- Funciona con cualquier tamaño de lista<br>- Error si lista vacía |
| HU-5 | Como operador, quiero agregar asteroides a una lista de seguimiento para monitorearlos | - No permite duplicados<br>- Confirmación visual al agregar |
| HU-6 | Como operador, quiero eliminar asteroides de la watchlist para limpiarla | - Confirmación si el ID no existe<br>- Lista actualizada inmediatamente |

**Entidades identificadas:**
- `NearEarthObject` — asteroide con id, nombre, diámetro, velocidad, miss_distance, fecha
- `WatchList` — colección en memoria de NEOs de interés

---

## Etapa 2 — Diseño (modo `Ask`)

**Prompt utilizado:**
```
Basándome en estas historias de usuario para un sistema NeoTracker en Python CLI,
propón:
1. Una arquitectura de módulos (sin frameworks externos)
2. Los comandos CLI que necesitaré exponer
3. Cómo estructurar las llamadas a la NASA NeoWs API
4. Un diagrama de flujo en ASCII

Lenguaje: Python 3.9+, sin dependencias externas (solo stdlib).
```

**Decisiones técnicas tomadas:**

| Decisión | Alternativa descartada | Razón |
|----------|------------------------|-------|
| Solo stdlib (`urllib`, `argparse`, `unittest`) | `requests`, `click`, `pytest` | Sin instalaciones adicionales facilita la ejecución en cualquier entorno |
| Módulos separados por responsabilidad | Todo en un solo archivo | Mejor testabilidad y mantenibilidad |
| `miss_distance.kilometers` como `float` | Comparar como string | La API devuelve el valor como string — hay que convertir explícitamente |
| CLI sobre REST API | FastAPI/Flask | Más rápido de implementar en 60 minutos |

**Arquitectura de módulos decidida:**
```
models.py         → Entidades de datos (NearEarthObject, WatchList)
nasa_client.py    → Capa HTTP y parsing del JSON de NASA
analyzer.py       → Lógica pura (sort, find_most_dangerous) — sin I/O
watchlist_service.py → Estado en memoria + operaciones CRUD
cli.py            → Interfaz de usuario, parseo de argumentos
```

---

## Etapa 3 — Desarrollo (modo `Agent`)

**Prompt de arranque:**
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

**Archivos generados:**
- [`src/models.py`](../../src/models.py) — `NearEarthObject` (dataclass), `WatchList`
- [`src/nasa_client.py`](../../src/nasa_client.py) — `fetch_neos()`, `_parse_neo()`, validación de rango
- [`src/analyzer.py`](../../src/analyzer.py) — `sort_by_size()`, `sort_by_velocity()`, `find_most_dangerous()`
- [`src/watchlist_service.py`](../../src/watchlist_service.py) — instancia global, add/remove/list
- [`src/cli.py`](../../src/cli.py) — argparse completo con subcomandos

**Corrección quirúrgica aplicada:**
```
La función find_most_dangerous() debe comparar miss_distance_km como float.
El campo viene como string desde el JSON de NASA — en _parse_neo() ya se
convierte con float(). Verificar que el dataclass lo almacene como float.
```

---

## Etapa 4 — Pruebas (modo `Agent`)

**Prompt utilizado:**
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
Incluye fixture con 5 NEOs mock con diferentes valores de tamaño, velocidad y distancia.
```

**Resultado:** 17 tests generados en [`tests/test_neotracker.py`](../../tests/test_neotracker.py)
- ✅ `TestSortByVelocity` (3 tests)
- ✅ `TestSortBySize` (3 tests)
- ✅ `TestFindMostDangerous` (4 tests)
- ✅ `TestWatchListAdd` (3 tests)
- ✅ `TestWatchListDuplicate` (2 tests)
- ✅ `TestWatchListRemove` (4 tests)

**Output esperado:**
```
test_add_multiple ... ok
test_add_returns_true ... ok
test_item_is_in_list ... ok
test_duplicate_returns_false ... ok
test_size_unchanged_after_duplicate ... ok
test_ascending_order (velocity) ... ok
test_descending_order (velocity) ... ok
test_preserves_all_elements ... ok
test_ascending_order (size) ... ok
test_descending_order (size) ... ok
test_first_is_largest ... ok
test_empty_list_raises ... ok
test_finds_minimum_miss_distance ... ok
test_miss_distance_is_float_comparison ... ok
test_single_element_list ... ok
test_item_no_longer_in_list ... ok
test_remove_all ... ok
test_remove_existing_returns_true ... ok
test_remove_nonexistent_returns_false ... ok

Ran 17 tests in 0.001s — OK
```

---

## Etapa 5 — Documentación (modo `Agent`)

**Prompt utilizado:**
```
Genera un README-solution.md completo para NeoTracker. Debe incluir:
1. Descripción del sistema
2. Tecnologías (solo stdlib Python)
3. Instalación y ejecución
4. Cómo obtener API key gratuita de NASA
5. Ejemplos de uso con comandos reales (fetch, danger, watch add/remove/list)
6. Estructura del proyecto
7. Cómo correr los tests
8. Arquitectura en ASCII

Basate en los archivos ya existentes en src/ y tests/.
Guárdalo como README-solution.md en la raíz del proyecto.
```

Archivo generado: [`README-solution.md`](../../README-solution.md)

---

## Etapa 6 — Entrega (modo `Agent`)

**Mensaje de commit generado con Bob:**
```
feat(neotracker): implement full NeoTracker system with CLI interface

- Add NearEarthObject and WatchList data models (src/models.py)
- Add NASA NeoWs API client with date range validation (src/nasa_client.py)
- Add analyzer module: sort by size/velocity, find most dangerous NEO (src/analyzer.py)
- Add in-memory watchlist service with add/remove/list operations (src/watchlist_service.py)
- Add CLI interface with fetch, danger, and watch subcommands (src/cli.py)
- Add 17 unit tests with mock data covering all business rules (tests/test_neotracker.py)
- Add complete README-solution.md with usage examples and architecture diagram
- Fill all evidence/ files documenting SDLC stages and Bob usage
```
