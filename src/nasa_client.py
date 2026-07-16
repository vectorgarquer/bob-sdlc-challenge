"""
nasa_client.py — Cliente para la NASA NeoWs API.
"""
import urllib.request
import urllib.parse
import json
from datetime import date, timedelta
from models import NearEarthObject


NASA_BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"


def _validate_date_range(start_date: str, end_date: str) -> None:
    """Valida que el rango de fechas sea válido y no supere 7 días."""
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    if end < start:
        raise ValueError("end_date debe ser mayor o igual a start_date.")
    if (end - start).days > 7:
        raise ValueError("El rango máximo permitido es 7 días.")


def _parse_neo(raw: dict) -> NearEarthObject:
    """Convierte un objeto raw del JSON de NASA en un NearEarthObject."""
    approach = raw["close_approach_data"][0]
    diameter = raw["estimated_diameter"]["kilometers"]
    return NearEarthObject(
        neo_id=raw["id"],
        name=raw["name"],
        estimated_diameter_km_min=float(diameter["estimated_diameter_min"]),
        estimated_diameter_km_max=float(diameter["estimated_diameter_max"]),
        is_potentially_hazardous=raw["is_potentially_hazardous_asteroid"],
        relative_velocity_kmh=float(approach["relative_velocity"]["kilometers_per_hour"]),
        miss_distance_km=float(approach["miss_distance"]["kilometers"]),
        close_approach_date=approach["close_approach_date"],
    )


def fetch_neos(start_date: str, end_date: str, api_key: str = "DEMO_KEY") -> list:
    """
    Consulta la NASA NeoWs API y retorna una lista de NearEarthObject.

    Args:
        start_date: Fecha de inicio en formato YYYY-MM-DD.
        end_date:   Fecha de fin en formato YYYY-MM-DD (máx. 7 días desde start).
        api_key:    NASA API key (default: DEMO_KEY).

    Returns:
        Lista de NearEarthObject ordenada por fecha de acercamiento.
    """
    _validate_date_range(start_date, end_date)

    params = urllib.parse.urlencode({
        "start_date": start_date,
        "end_date": end_date,
        "api_key": api_key,
    })
    url = f"{NASA_BASE_URL}?{params}"

    with urllib.request.urlopen(url, timeout=15) as response:
        data = json.loads(response.read().decode())

    neos = []
    for day_neos in data["near_earth_objects"].values():
        for raw in day_neos:
            neos.append(_parse_neo(raw))

    return neos
