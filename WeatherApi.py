import requests
import json

r = requests.get('http://api.openweathermap.org/data/2.5/weather?appid={your key}&q=ashdod')
json_data = r.json()
print(json_data)