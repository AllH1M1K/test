# Вариант: Москва
import requests
city = "Moscow"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f10ef0e2eff90f6cfea9afa5b2bb516f"


response = requests.get(url)
data = response.json()

temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["description"]
pressure = data["main"]["pressure"]
wind = data["wind"]["speed"]

print(f"Погода в городе {city}:")
print(f"Температура: {temperature}°C")
print(f"Влажность: {humidity}%")
print(f"Погода: {weather}")
print(f"Давление: {pressure} мм рт. ст.")
print(f"Ветер: {wind} м/c")