"""
models.py — Entidades de datos del sistema NeoTracker.
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NearEarthObject:
    """Representa un asteroide NEO extraído de la NASA NeoWs API."""
    neo_id: str
    name: str
    estimated_diameter_km_min: float
    estimated_diameter_km_max: float
    is_potentially_hazardous: bool
    relative_velocity_kmh: float
    miss_distance_km: float
    close_approach_date: str

    @property
    def estimated_diameter_km_avg(self) -> float:
        return (self.estimated_diameter_km_min + self.estimated_diameter_km_max) / 2

    def to_dict(self) -> dict:
        return {
            "id": self.neo_id,
            "name": self.name,
            "diameter_km_avg": round(self.estimated_diameter_km_avg, 4),
            "diameter_km_min": round(self.estimated_diameter_km_min, 4),
            "diameter_km_max": round(self.estimated_diameter_km_max, 4),
            "is_potentially_hazardous": self.is_potentially_hazardous,
            "relative_velocity_kmh": round(self.relative_velocity_kmh, 2),
            "miss_distance_km": round(self.miss_distance_km, 2),
            "close_approach_date": self.close_approach_date,
        }


@dataclass
class WatchList:
    """Lista de seguimiento de asteroides en memoria."""
    _items: dict = field(default_factory=dict)

    def add(self, neo: NearEarthObject) -> bool:
        """Agrega un NEO. Retorna False si ya existe."""
        if neo.neo_id in self._items:
            return False
        self._items[neo.neo_id] = neo
        return True

    def remove(self, neo_id: str) -> bool:
        """Elimina un NEO por ID. Retorna False si no existe."""
        if neo_id not in self._items:
            return False
        del self._items[neo_id]
        return True

    def list_all(self) -> list:
        return list(self._items.values())

    def get(self, neo_id: str) -> Optional[NearEarthObject]:
        return self._items.get(neo_id)

    def __len__(self) -> int:
        return len(self._items)
