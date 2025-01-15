import requests

api_key = 'c71335fdf44d7674e2eec28e2f206341'
city = 'Melbourne, AU'
url = f'https://api.openweathermap.org/data/2.5/weather?q=Melbourne&appid={api_key}'

res = requests.get(url)
data = res.json()


print(data.get('main'))
print(data.get('main').get('temp'))

