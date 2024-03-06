import requests
import time

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.weatherapi.com/v1/current.json"
        self.favorites = []

    def get_weather(self, city):
        response = requests.get(f"{self.base_url}?key={self.api_key}&q={city}")
        return response.json()

    def add_favorite(self, city):
        if city not in self.favorites:
            self.favorites.append(city)

    def remove_favorite(self, city):
        if city in self.favorites:
            self.favorites.remove(city)

    def update_weather(self):
        while True:
            for city in self.favorites:
                print(self.get_weather(city))
            time.sleep(15)  # refresh every 15 seconds

    def run(self):
        while True:
            print("1. Check weather")
            print("2. Add city to favorites")
            print("3. Remove city from favorites")
            print("4. View favorite cities")
            print("5. Auto-refresh weather for favorite cities")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                city = input("Enter city name: ")
                print(self.get_weather(city))
            elif choice == '2':
                city = input("Enter city name: ")
                self.add_favorite(city)
            elif choice == '3':
                city = input("Enter city name: ")
                self.remove_favorite(city)
            elif choice == '4':
                print(self.favorites)
            elif choice == '5':
                self.update_weather()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

app = WeatherApp('7da95365fd104c83980144636240503')
app.run()
