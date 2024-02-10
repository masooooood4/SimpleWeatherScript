from data import WEATHER_DATA

def get_weather(city):
    data = WEATHER_DATA.get(city.title(),"no data available for this city")
    return data["temperature"] , data["condition"]

def get_recomendation(condition):
    if condition =="rainy":
        return "dont forget umbrella"
    elif condition =="sunny":
        return "wear some sunscreen!"
    else:
        return "have a great day"

def present_info(name,temp,condition):
    print(f" in {name}, current temprature is : {temp} and the condition is : {condition}")
    

def main():
    city = input("enter the name of the city to get its current weather: ")
    temp,condition = get_weather(city)
    present_info(city,temp,condition)

if __name__ == "__main__":
    main()