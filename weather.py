import requests

api_key = '&appid=84de577cbd32a5c65d6c79767729a2cf'
api_key_temp = '&appid=67da29cb91129f1a68c1c06c1be92daa'
zip = '78738,us'
city = 'Bee Cave'
url = 'http://api.openweathermap.org/data/2.5/weather?'
units = '&units=imperial'
urlCity = url+'q='+city+api_key_temp+units
urlZip = url+'zip='+zip+api_key_temp+units

response = requests.get(urlZip)
json = response.json()

desc = json.get("weather")[0].get("description")
print("Forecast:", desc)
temp_min = json.get('main')['temp_min']
print("Min Temp:", temp_min,'F')
temp_max = json.get('main')['temp_max']
print("Max Temp:", temp_max,'F')
temp_cur = json.get('main')['temp']
print('Current Temp: ',temp_cur)
