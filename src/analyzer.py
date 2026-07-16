"""
analyzer.py — Lógica de análisis y ordenamiento de NEOs.
"""
from models import NearEarthObject


def sort_by_size(neos: list, descending: bool = True) -> list:
    """
    Ordena una lista de NEOs por diámetro promedio estimado.

    Args:
        neos:       Lista de NearEarthObject.
        descending: True para mayor primero (default), False para menor primero.

    Returns:
        Nueva lista ordenada.
    """
    return sorted(neos, key=lambda n: n.estimated_diameter_km_avg, reverse=descending)


def sort_by_velocity(neos: list, descending: bool = False) -> list:
    """
    Ordena una lista de NEOs por velocidad relativa en km/h.

    Args:
        neos:       Lista de NearEarthObject.
        descending: False para menor primero/más lento (default), True para mayor primero.

    Returns:
        Nueva lista ordenada.
    """
    return sorted(neos, key=lambda n: n.relative_velocity_kmh, reverse=descending)


def find_most_dangerous(neos: list) -> NearEarthObject:
    """
    Identifica el asteroide más peligroso: el de menor miss_distance_km.

    Args:
        neos: Lista de NearEarthObject (debe tener al menos un elemento).

    Returns:
        El NearEarthObject con la menor distancia de acercamiento a la Tierra.

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not neos:
        raise ValueError("La lista de NEOs está vacía.")
    return min(neos, key=lambda n: n.miss_distance_km)
