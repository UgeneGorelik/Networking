import requests
import json

r = requests.get('http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=ashdod')
json_data = r.json()
print(json_data)