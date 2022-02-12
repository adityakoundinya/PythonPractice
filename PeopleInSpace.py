import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

for i in json['people']:
  print(i['name'], 'in', i['craft'])
