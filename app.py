import requests
import json
import os


API_KEY = "e81e4bee64bc4c022185de5b9af6d536"
FILE_NAME = "history.json"
# city = "kathmandu"


def search_weather():
    
    city_name = input("Enter the city name: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    # print(data)
    if response.status_code == 200:

        city = data["name"]
        temperature= data["main"]["temp"]
        humidity=data["main"]["humidity"]
        weather=data["weather"][0]["main"]

        print(f"City: {city}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Weather: {weather}")

        weather_record = {
            "name":city,
            "temperature": temperature,
            "humidity": humidity,
            "weather": weather
        }

        history = []

        if os.path.exists("history.json"):
            with open("history.json", "r") as file:
                history = json.load(file)

        history.append(weather_record)  


        with open("history.json","w") as file:
            json.dump(history,file,indent=4)

        print("Data saved to history.json")  

    else: 
        print("Information not found.")       

def view_history():
    if not os.path.exists(FILE_NAME):
        print("History not found.")  
        return
    
    with open(FILE_NAME, "r") as file:
        history = json.load(file)

    print("Search history")

    for index, record in enumerate(history, start=1):
        print(
            f"{index}. "
            f"{record['city']} | "
            f"{record['temperature']}°C | "
            f"{record['weather']}"
        )

def delete_history():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("History deleted..")
    else:
        print("History not found") 

def main():
    while True:
        print("Enter your choice:")
        print("1. Search weather")
        print("2. View history")
        print("3. Delete history")
        print("4. Exit")

        choice = input("Enter your choice.")

        if choice == "1":
            search_weather()
        elif choice == 2:
            view_history()
        elif choice == 3:
            delete_history
        elif choice == 4:
            break
        else:
            print("Invalid input.")


main()
   





        