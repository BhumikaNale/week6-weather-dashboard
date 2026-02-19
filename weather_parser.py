from datetime import datetime


def parse_current(data: dict) -> dict:
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "condition": data["weather"][0]["description"].title(),
        "icon": data["weather"][0]["main"],
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }


def parse_forecast(data: dict) -> list:
    daily = {}

    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]
        temp = item["main"]["temp"]

        if date not in daily:
            daily[date] = {"temps": [], "condition": item["weather"][0]["main"]}

        daily[date]["temps"].append(temp)

    result = []
    for date, info in list(daily.items())[:5]:
        result.append({
            "date": date,
            "min": round(min(info["temps"]), 1),
            "max": round(max(info["temps"]), 1),
            "condition": info["condition"]
        })

    return result

