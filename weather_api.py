import requests
import json
import time
from pathlib import Path
from typing import Optional, Dict
from .config import API_KEY, BASE_URL, CACHE_DIR
    
class WeatherAPI:
    def __init__(self):
        self.api_key = API_KEY
        self.cache_duration = 600

    def _cache_file(self, key: str) -> Path:
        return CACHE_DIR / f"{key}.json"

    def _get_cache(self, key: str) -> Optional[Dict]:
        file = self._cache_file(key)
        if file.exists():
            if time.time() - file.stat().st_mtime < self.cache_duration:
                try:
                    return json.loads(file.read_text())
                except:
                    return None
        return None

    def _save_cache(self, key: str, data: Dict):
        try:
            self._cache_file(key).write_text(json.dumps(data))
        except:
            pass

    def _request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        try:
            params["appid"] = self.api_key
            params["units"] = "metric"

            res = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=10)

            if res.status_code == 200:
                return res.json()
            elif res.status_code == 404:
                print("❌ City not found")
            elif res.status_code == 401:
                print("❌ Invalid API key")
            else:
                print("❌ API Error:", res.status_code)

        except requests.exceptions.RequestException:
            print("❌ Network error")

        return None

    def current_weather(self, city: str) -> Optional[Dict]:
        key = f"current_{city}"
        cached = self._get_cache(key)
        if cached:
            return cached

        data = self._request("weather", {"q": city})
        if data:
            self._save_cache(key, data)
        return data

    def forecast(self, city: str) -> Optional[Dict]:
        key = f"forecast_{city}"
        cached = self._get_cache(key)
        if cached:
            return cached

        data = self._request("forecast", {"q": city})
        if data:
            self._save_cache(key, data)
        return data
