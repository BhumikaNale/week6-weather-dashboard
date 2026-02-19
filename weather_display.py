from colorama import Fore, Style


ICONS = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Snow": "❄️",
    "Thunderstorm": "⛈️"
}


def show_current(data: dict):
    print("\n🌤️ WEATHER DASHBOARD")
    print("=" * 30)
    print(f"📍 {data['city']}, {data['country']}")
    print(f"🕐 {data['time']}\n")

    print("Current Weather")
    print("-" * 30)

    color = Fore.RED if data["temp"] > 30 else Fore.CYAN

    print(f"Temp: {color}{data['temp']}°C{Style.RESET_ALL} (Feels {data['feels_like']}°C)")
    print(f"Condition: {data['condition']} {ICONS.get(data['icon'], '')}")
    print(f"Humidity: {data['humidity']}%")
    print(f"Wind: {data['wind']} m/s")


def show_forecast(forecast: list):
    print("\n5-Day Forecast")
    print("-" * 30)
    for day in forecast:
        icon = ICONS.get(day["condition"], "")
        print(f"{day['date']} | {icon} {day['min']}°C - {day['max']}°C")
