from fastapi import APIRouter, HTTPException, Response

from app.services import watchlist_service

router = APIRouter(prefix="/watchlist", tags=["Watchlist"])


@router.get(
    "",
    response_model=list[str],
    summary="Get watchlist",
    description="Returns all asteroid IDs currently in the tracking list.",
)
def get_watchlist():
    return watchlist_service.get_all()


@router.post(
    "/{asteroid_id}",
    status_code=201,
    summary="Add asteroid to watchlist",
    description="Adds an asteroid ID to the in-memory tracking list.",
    responses={
        201: {"description": "Asteroid added to watchlist"},
        409: {"description": "Asteroid already in watchlist"},
    },
)
def add_to_watchlist(asteroid_id: str):
    if watchlist_service.exists(asteroid_id):
        raise HTTPException(
            status_code=409,
            detail=f"Asteroid '{asteroid_id}' is already in the watchlist.",
        )
    watchlist_service.add(asteroid_id)
    return {"detail": f"Asteroid '{asteroid_id}' added to watchlist."}


@router.delete(
    "/{asteroid_id}",
    status_code=204,
    summary="Remove asteroid from watchlist",
    description="Removes an asteroid ID from the in-memory tracking list.",
    responses={
        204: {"description": "Asteroid removed"},
        404: {"description": "Asteroid not found in watchlist"},
    },
)
def remove_from_watchlist(asteroid_id: str):
    if not watchlist_service.exists(asteroid_id):
        raise HTTPException(
            status_code=404,
            detail=f"Asteroid '{asteroid_id}' not found in watchlist.",
        )
    watchlist_service.remove(asteroid_id)
    return Response(status_code=204)
