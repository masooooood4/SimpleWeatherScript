from data import WEATHER_DATA

def get_weather(city,show_recomendation):

    data = WEATHER_DATA.get(city.title(), "no data available for this city")
    if show_recomendation:
        recomendation = get_recomendation(data["condition"])
    else:
        recomendation =None
    return data["temperature"] , data["condition"],recomendation

def get_recomendation(condition):
    if condition =="rainy":
        return "dont forget umbrella"
    elif condition =="sunny":
        return "wear some sunscreen!"
    else:
        return "have a great day"

def present_info(name,temp,condition,final_recomendation):
    print(f"in {name}, current temprature is : {temp} and the condition is : {condition}")
    if final_recomendation is not None:
        print(f"and our recomendation is: {final_recomendation}")

def main():
    city = input("enter the name of the city to get its current weather: ")
    wants_recomendations = input("do you want to see our recomendation for today?(y/n)")
    if wants_recomendations=="y":
        show_recomendation =True
    else:
        show_recomendation =False
    temp,condition,final_recomendation = get_weather(city,show_recomendation)
    present_info(city,temp,condition,final_recomendation)
    

if __name__ == "__main__":
    main()