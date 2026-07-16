import httpx
from app.config import NASA_API_KEY, NASA_BASE_URL
from app.models.asteroid import NearEarthObject
from fastapi import HTTPException


async def fetch_asteroids(start_date: str, end_date: str) -> list[NearEarthObject]:
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": NASA_API_KEY,
    }

    async with httpx.AsyncClient(timeout=15.0) as client:
        try:
            response = await client.get(NASA_BASE_URL, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=502,
                detail=f"NASA API error: {e.response.status_code} {e.response.text}",
            )
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=502,
                detail=f"Could not reach NASA API: {str(e)}",
            )

    data = response.json()
    raw_by_date: dict = data.get("near_earth_objects", {})

    asteroids: list[NearEarthObject] = []
    for daily_list in raw_by_date.values():
        for obj in daily_list:
            approach = obj["close_approach_data"][0]
            diameter = obj["estimated_diameter"]["kilometers"]
            asteroids.append(
                NearEarthObject(
                    id=obj["id"],
                    name=obj["name"],
                    nasa_jpl_url=obj["nasa_jpl_url"],
                    is_potentially_hazardous=obj["is_potentially_hazardous_asteroid"],
                    estimated_diameter_min_km=float(diameter["estimated_diameter_min"]),
                    estimated_diameter_max_km=float(diameter["estimated_diameter_max"]),
                    relative_velocity_km_h=float(
                        approach["relative_velocity"]["kilometers_per_hour"]
                    ),
                    miss_distance_km=float(approach["miss_distance"]["kilometers"]),
                    close_approach_date=approach["close_approach_date"],
                )
            )

    return asteroids
