import requests

apiKey = "3091a9532ae0a303182c0a908bc671bc"
city = input("What city? : ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"

response = requests.get(url)
data = response.json()

try:
  data["main"]
except:
  print("City doesn't exist")
  exit()

temp = data["main"]["temp"]
temp = (temp - 273.15) * (9 / 5) + 32
weather = data['weather'][0]['description']
humidity = data['main']['humidity']

print(f"\nTemperature: {round(temp, 1)} f")
print(f"Weather: {weather}")
print(f"Humidity: {humidity}%")
