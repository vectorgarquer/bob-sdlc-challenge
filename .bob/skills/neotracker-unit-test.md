---
name: neotracker-unit-test
description: Genera tests unitarios para NeoTracker con datos mock. Usa unittest (stdlib), fixtures de NearEarthObject, sin llamadas reales a la NASA API. Activa esta skill cuando necesites escribir o extender tests del proyecto NeoTracker.
---

# NeoTracker — Test Generator

Cuando generes tests para este proyecto, sigue siempre estas reglas:

## Imports y setup

```python
import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from models import NearEarthObject, WatchList
from analyzer import sort_by_size, sort_by_velocity, find_most_dangerous
```

## Fixture obligatorio

Usa siempre un helper `make_neo()` en lugar de instanciar `NearEarthObject` directamente:

```python
def make_neo(neo_id, name, diameter_min, diameter_max, velocity_kmh, miss_distance_km,
             hazardous=False, approach_date="2025-01-01"):
    return NearEarthObject(
        neo_id=neo_id, name=name,
        estimated_diameter_km_min=diameter_min,
        estimated_diameter_km_max=diameter_max,
        is_potentially_hazardous=hazardous,
        relative_velocity_kmh=velocity_kmh,
        miss_distance_km=miss_distance_km,
        close_approach_date=approach_date,
    )
```

## Reglas de escritura de tests

1. **Framework:** `unittest.TestCase` — no pytest puro (solo stdlib, sin pip install)
2. **Sin llamadas reales:** Nunca llames a `fetch_neos()` — solo prueba lógica pura
3. **Casos borde obligatorios:** lista vacía, duplicados, IDs inexistentes
4. **Nomenclatura:** clases `Test<Modulo>`, métodos `test_<caso_descripcion>`
5. **setUp:** usa `self.wl = WatchList()` en `setUp` cuando hay estado compartido
6. **Aserciones:** usa `assertEqual`, `assertTrue`, `assertFalse`, `assertIsNone`, `assertRaises`

## Estructura mínima esperada por módulo

- `analyzer.py` → `TestSortByVelocity`, `TestSortBySize`, `TestFindMostDangerous`
- `models.py (WatchList)` → `TestWatchListAdd`, `TestWatchListDuplicate`, `TestWatchListRemove`

## Ejemplo de test correcto

```python
class TestFindMostDangerous(unittest.TestCase):
    def test_finds_minimum_miss_distance(self):
        neos = [make_neo("1", "A", 0.1, 0.2, 50000, 500000),
                make_neo("2", "B", 0.4, 0.8, 30000,  50000)]  # B es más peligroso
        result = find_most_dangerous(neos)
        self.assertEqual(result.neo_id, "2")

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            find_most_dangerous([])
```
