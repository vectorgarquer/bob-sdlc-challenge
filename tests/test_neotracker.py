"""
test_neotracker.py — Tests unitarios de NeoTracker (sin llamadas reales a la NASA API).

Ejecutar con:
    python -m pytest tests/ -v
    # o directamente:
    python tests/test_neotracker.py
"""
import sys
import os
import unittest

# Permite importar desde src/ sin instalar el paquete
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from models import NearEarthObject, WatchList
from analyzer import sort_by_size, sort_by_velocity, find_most_dangerous


# ---------------------------------------------------------------------------
# Fixtures de datos mock
# ---------------------------------------------------------------------------

def make_neo(neo_id, name, diameter_min, diameter_max, velocity_kmh, miss_distance_km,
             hazardous=False, approach_date="2025-01-01"):
    return NearEarthObject(
        neo_id=neo_id,
        name=name,
        estimated_diameter_km_min=diameter_min,
        estimated_diameter_km_max=diameter_max,
        is_potentially_hazardous=hazardous,
        relative_velocity_kmh=velocity_kmh,
        miss_distance_km=miss_distance_km,
        close_approach_date=approach_date,
    )


ALPHA   = make_neo("1", "Alpha",   0.1,  0.2,  50000,  500000)
BETA    = make_neo("2", "Beta",    0.4,  0.8,  30000,  200000)
GAMMA   = make_neo("3", "Gamma",   0.01, 0.05, 80000, 1500000)
DELTA   = make_neo("4", "Delta",   1.0,  2.0,  20000,   50000, hazardous=True)
EPSILON = make_neo("5", "Epsilon", 0.05, 0.1,  60000,  800000)

SAMPLE_LIST = [ALPHA, BETA, GAMMA, DELTA, EPSILON]


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestSortByVelocity(unittest.TestCase):
    """Caso 1: Ordenar por velocidad relativa ascendente."""

    def test_ascending_order(self):
        result = sort_by_velocity(SAMPLE_LIST, descending=False)
        velocities = [n.relative_velocity_kmh for n in result]
        self.assertEqual(velocities, sorted(velocities))

    def test_descending_order(self):
        result = sort_by_velocity(SAMPLE_LIST, descending=True)
        velocities = [n.relative_velocity_kmh for n in result]
        self.assertEqual(velocities, sorted(velocities, reverse=True))

    def test_preserves_all_elements(self):
        result = sort_by_velocity(SAMPLE_LIST)
        self.assertEqual(len(result), len(SAMPLE_LIST))


class TestSortBySize(unittest.TestCase):
    """Caso 2: Ordenar por tamaño estimado descendente."""

    def test_descending_order(self):
        result = sort_by_size(SAMPLE_LIST, descending=True)
        diameters = [n.estimated_diameter_km_avg for n in result]
        self.assertEqual(diameters, sorted(diameters, reverse=True))

    def test_ascending_order(self):
        result = sort_by_size(SAMPLE_LIST, descending=False)
        diameters = [n.estimated_diameter_km_avg for n in result]
        self.assertEqual(diameters, sorted(diameters))

    def test_first_is_largest(self):
        result = sort_by_size(SAMPLE_LIST, descending=True)
        # DELTA tiene diámetro avg 1.5 km — el mayor
        self.assertEqual(result[0].neo_id, "4")


class TestFindMostDangerous(unittest.TestCase):
    """Caso 3: Identificar el de menor miss_distance."""

    def test_finds_minimum_miss_distance(self):
        result = find_most_dangerous(SAMPLE_LIST)
        # DELTA tiene miss_distance_km = 50000 — el menor
        self.assertEqual(result.neo_id, "4")

    def test_single_element_list(self):
        result = find_most_dangerous([ALPHA])
        self.assertEqual(result.neo_id, "1")

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            find_most_dangerous([])

    def test_miss_distance_is_float_comparison(self):
        # Verifica que la comparación sea numérica (no de strings)
        neo_a = make_neo("A", "A", 0.1, 0.2, 10000, 9000.5)
        neo_b = make_neo("B", "B", 0.1, 0.2, 10000, 90000.0)
        result = find_most_dangerous([neo_b, neo_a])
        self.assertEqual(result.neo_id, "A")


class TestWatchListAdd(unittest.TestCase):
    """Caso 4: Agregar un asteroide a la lista de seguimiento."""

    def setUp(self):
        self.wl = WatchList()

    def test_add_returns_true(self):
        result = self.wl.add(ALPHA)
        self.assertTrue(result)

    def test_item_is_in_list(self):
        self.wl.add(ALPHA)
        self.assertEqual(len(self.wl), 1)
        self.assertIsNotNone(self.wl.get(ALPHA.neo_id))

    def test_add_multiple(self):
        self.wl.add(ALPHA)
        self.wl.add(BETA)
        self.assertEqual(len(self.wl), 2)


class TestWatchListDuplicate(unittest.TestCase):
    """Caso 5: Agregar un duplicado debe ignorarse."""

    def setUp(self):
        self.wl = WatchList()

    def test_duplicate_returns_false(self):
        self.wl.add(ALPHA)
        result = self.wl.add(ALPHA)
        self.assertFalse(result)

    def test_size_unchanged_after_duplicate(self):
        self.wl.add(ALPHA)
        self.wl.add(ALPHA)
        self.assertEqual(len(self.wl), 1)


class TestWatchListRemove(unittest.TestCase):
    """Caso 6: Eliminar un asteroide que existe."""

    def setUp(self):
        self.wl = WatchList()
        self.wl.add(ALPHA)
        self.wl.add(BETA)

    def test_remove_existing_returns_true(self):
        result = self.wl.remove(ALPHA.neo_id)
        self.assertTrue(result)

    def test_item_no_longer_in_list(self):
        self.wl.remove(ALPHA.neo_id)
        self.assertIsNone(self.wl.get(ALPHA.neo_id))
        self.assertEqual(len(self.wl), 1)

    def test_remove_nonexistent_returns_false(self):
        result = self.wl.remove("nonexistent_id")
        self.assertFalse(result)

    def test_remove_all(self):
        self.wl.remove(ALPHA.neo_id)
        self.wl.remove(BETA.neo_id)
        self.assertEqual(len(self.wl), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
