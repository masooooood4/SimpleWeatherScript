from data import WEATHER_DATA

def get_weather(city):

    return WEATHER_DATA.get(city.title(),"no data available for this city")

def get_recomendation(condition):
    if condition =="rainy":
        return "dont forget umbrella"
    elif condition =="sunny":
        return "wear some sunscreen!"
    else:
        return "have a great day"


def main():
    city = input("enter the name of the city to get its current weather: ")
    weather = get_weather(city)
    print(weather)
    print(f"weather in {city.title()}: {weather}")

if __name__ == "__main__":
    main()