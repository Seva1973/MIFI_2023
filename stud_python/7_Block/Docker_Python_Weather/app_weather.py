import requests

API_KEY = "f2222cab4aad4a164742d76a3c01f561"

city_name = input("Введите название города: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    weather_description = data["weather"][0]["description"]
    print(f"Текущая температура в городе {city_name}: {temp}°C")
    print(f"Состояние погоды: {weather_description}")
else:
    print("Ошибка при получении данных о погоде")

