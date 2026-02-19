import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5"

CACHE_DIR = Path("data/cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

FAVORITES_FILE = Path("data/favorites.json")
FAVORITES_FILE.parent.mkdir(parents=True, exist_ok=True)

if not FAVORITES_FILE.exists():
    FAVORITES_FILE.write_text("[]")
