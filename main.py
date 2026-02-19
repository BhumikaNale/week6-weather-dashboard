import json
from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import parse_current, parse_forecast
from weather_app.weather_display import show_current, show_forecast
from weather_app.config import FAVORITES_FILE
from weather_app.config import API_KEY
print("API KEY =", API_KEY)



api = WeatherAPI()


def load_favorites():
    return json.loads(FAVORITES_FILE.read_text())


def save_favorites(favs):
    FAVORITES_FILE.write_text(json.dumps(favs))


def add_favorite(city):
    favs = load_favorites()
    if city not in favs:
        favs.append(city)
        save_favorites(favs)
        print("⭐ Added to favorites")


def show_menu():
    print("\nMenu:")
    print("1. Search city")
    print("2. Show favorites")
    print("3. Add favorite")
    print("4. Exit")


def search_city():
    city = input("Enter city: ")
    current = api.current_weather(city)
    if not current:
        return

    forecast = api.forecast(city)

    current_data = parse_current(current)
    forecast_data = parse_forecast(forecast)

    show_current(current_data)
    show_forecast(forecast_data)


def show_favorites():
    favs = load_favorites()
    if not favs:
        print("No favorites yet")
        return

    for city in favs:
        current = api.current_weather(city)
        if current:
            data = parse_current(current)
            print(f"{data['city']}: {data['temp']}°C, {data['condition']}")


def main():
    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            search_city()
        elif choice == "2":
            show_favorites()
        elif choice == "3":
            city = input("City to add: ")
            add_favorite(city)
        elif choice == "4":
            print("👋 Bye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
