from data import WEATHER_DATA

def get_weather(city):

    return WEATHER_DATA.get(city.title(),"no data available for this city")


def main():
    city = input("enter the name of the city to get its current weather: ")
    weather = get_weather(city)
    print(weather)
    print(f"weather in {city.title()}: {weather}")

if __name__ == "__main__":
    main()