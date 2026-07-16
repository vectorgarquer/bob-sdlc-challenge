from pydantic import BaseModel


class NearEarthObject(BaseModel):
    id: str
    name: str
    nasa_jpl_url: str
    is_potentially_hazardous: bool
    estimated_diameter_min_km: float
    estimated_diameter_max_km: float
    relative_velocity_km_h: float
    miss_distance_km: float
    close_approach_date: str
