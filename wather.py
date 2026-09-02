import requests
city = input("enter location")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={'f39e88433520077bfeb9c904c5a5b579'}&units=metric"
response = requests.get(url)

wather = response.json()

print(wather["weather"][0]["main"])