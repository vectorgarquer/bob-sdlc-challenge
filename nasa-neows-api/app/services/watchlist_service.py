from typing import Set

_watchlist: Set[str] = set()


def get_all() -> list[str]:
    return sorted(_watchlist)


def add(asteroid_id: str) -> None:
    _watchlist.add(asteroid_id)


def remove(asteroid_id: str) -> None:
    _watchlist.discard(asteroid_id)


def exists(asteroid_id: str) -> bool:
    return asteroid_id in _watchlist
