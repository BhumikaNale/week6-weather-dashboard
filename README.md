🌤️ Weather Dashboard Application

A command-line weather dashboard built in Python that fetches real-time weather data using the OpenWeather API.
It displays current weather, 5-day forecast, supports favorites, caching, and error handling.

> Features

✅ Fetch current weather for any city worldwide
✅ Display temperature, humidity, wind speed, and conditions
✅ 5-day weather forecast
✅ Add and view favorite cities
✅ API response caching (reduces API calls)
✅ Celsius temperature display
✅ Error handling for invalid city/API/network issues
✅ User-friendly command-line menu

> Tech Stack
Python 3
OpenWeatherMap API
Requests
python-dotenv
JSON for caching & favorites

> Project Structure
week6-weather-dashboard/
│── weather_app/
│   ├── __init__.py
│   ├── config.py
│   ├── weather_api.py
│   ├── weather_parser.py
│   ├── weather_display.py
│   └── main.py
│── data/
│   ├── cache/
│   └── favorites.json
│── requirements.txt
│── .env.example
│── README.md

⚙️ Setup Instructions
> Clone the repository
git clone https://github.com/your-username/week6-weather-dashboard.git
cd week6-weather-dashboard

> Install dependencies
pip install -r requirements.txt

> Get OpenWeather API Key
Go to https://openweathermap.org
Sign up → My API Keys
Copy your API key

> Create .env file
Create a file in the project root:

>.env
Add:
OPENWEATHER_API_KEY=f6b53807656a31c2b09a9cdea8df7daf

> Run the Application
Run from project root:
python -m weather_app.main

>Menu Options
1. Search city weather
2. Show favorite cities weather
3. Add city to favorites
4. Exit

>Sample Output
🌤️ WEATHER DASHBOARD

Menu:
1. Search city
2. Show favorites
3. Add favorite
4. Exit
Choose: 1
Enter city: Mumbai

🌤️ WEATHER DASHBOARD
==============================
📍 Mumbai, IN
🕐 2026-02-20 00:24

Current Weather
------------------------------
Temp: 25.99°C (Feels 25.99°C)
Condition: Haze
Humidity: 73%
Wind: 3.09 m/s

5-Day Forecast
------------------------------
2026-02-19 | ☁️ 25.7°C - 25.7°C
2026-02-20 | ☁️ 25.6°C - 26.9°C
2026-02-21 | ☁️ 25.5°C - 27.3°C
2026-02-22 | ☁️ 25.0°C - 26.8°C
2026-02-23 | ☀️ 24.5°C - 26.1°C


> Error Handling
The app handles:
Invalid API key
City not found
Network errors
API rate limits

> Caching
API responses are cached for 10 minutes inside:
data/cache/
This reduces API calls and improves performance.

> Favorites
Favorite cities are stored in:
data/favorites.json
You can add multiple cities and view their weather quickly.

> Requirements
requests
python-dotenv

> Future Enhancements
Temperature unit toggle (°C ⇄ °F)
CSV export of weather data
Auto-detect location by IP

Weather comparison between cities

GUI version using Tkinter
