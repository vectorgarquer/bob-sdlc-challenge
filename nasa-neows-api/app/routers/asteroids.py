from datetime import datetime
from typing import Literal, Optional

from fastapi import APIRouter, HTTPException, Query

from app.models.asteroid import NearEarthObject
from app.services.nasa_service import fetch_asteroids

router = APIRouter(prefix="/asteroids", tags=["Asteroids"])

SORT_FIELDS = {
    "size_max": lambda a: a.estimated_diameter_max_km,
    "size_min": lambda a: a.estimated_diameter_min_km,
    "velocity": lambda a: a.relative_velocity_km_h,
}


def _parse_date(date_str: str, field: str) -> datetime:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid format for '{field}'. Expected YYYY-MM-DD.",
        )


@router.get(
    "/most-dangerous",
    response_model=NearEarthObject,
    summary="Get the most dangerous asteroid",
    description="Returns the asteroid with the smallest miss distance to Earth in the given date range.",
    responses={
        400: {"description": "Invalid date range"},
        404: {"description": "No asteroids found in the given range"},
        502: {"description": "NASA API error"},
    },
)
async def most_dangerous(
    start_date: str = Query(..., example="2024-01-01"),
    end_date: str = Query(..., example="2024-01-07"),
):
    start = _parse_date(start_date, "start_date")
    end = _parse_date(end_date, "end_date")

    if end < start:
        raise HTTPException(status_code=400, detail="end_date must be >= start_date.")
    if (end - start).days > 7:
        raise HTTPException(status_code=400, detail="Date range cannot exceed 7 days.")

    asteroids = await fetch_asteroids(start_date, end_date)

    if not asteroids:
        raise HTTPException(
            status_code=404, detail="No asteroids found in the given date range."
        )

    return min(asteroids, key=lambda a: a.miss_distance_km)


@router.get(
    "",
    response_model=list[NearEarthObject],
    summary="List near-Earth asteroids",
    description="Query asteroids in a date range (max 7 days). Optionally sort by size or velocity.",
    responses={
        400: {"description": "Invalid date range"},
        502: {"description": "NASA API error"},
    },
)
async def list_asteroids(
    start_date: str = Query(..., example="2024-01-01"),
    end_date: str = Query(..., example="2024-01-07"),
    sort_by: Optional[Literal["size_max", "size_min", "velocity"]] = Query(
        default=None, description="Field to sort by"
    ),
    order: Literal["asc", "desc"] = Query(default="desc", description="Sort order"),
):
    start = _parse_date(start_date, "start_date")
    end = _parse_date(end_date, "end_date")

    if end < start:
        raise HTTPException(status_code=400, detail="end_date must be >= start_date.")
    if (end - start).days > 7:
        raise HTTPException(status_code=400, detail="Date range cannot exceed 7 days.")

    asteroids = await fetch_asteroids(start_date, end_date)

    if sort_by:
        asteroids.sort(
            key=SORT_FIELDS[sort_by],
            reverse=(order == "desc"),
        )

    return asteroids
