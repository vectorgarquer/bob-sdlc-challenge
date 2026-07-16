"""
watchlist_service.py — Servicio de gestión de la lista de seguimiento.
"""
from models import WatchList, NearEarthObject

# Instancia global en memoria (única durante la sesión)
_watchlist = WatchList()


def get_watchlist() -> WatchList:
    return _watchlist


def add_to_watchlist(neo: NearEarthObject) -> dict:
    added = _watchlist.add(neo)
    if added:
        return {"status": "added", "id": neo.neo_id, "name": neo.name}
    return {"status": "duplicate", "id": neo.neo_id, "name": neo.name}


def remove_from_watchlist(neo_id: str) -> dict:
    removed = _watchlist.remove(neo_id)
    if removed:
        return {"status": "removed", "id": neo_id}
    return {"status": "not_found", "id": neo_id}


def list_watchlist() -> list:
    return [neo.to_dict() for neo in _watchlist.list_all()]
