import os
from dotenv import load_dotenv

load_dotenv()

NASA_API_KEY: str = os.getenv("NASA_API_KEY", "DEMO_KEY")
NASA_BASE_URL: str = "https://api.nasa.gov/neo/rest/v1/feed"
