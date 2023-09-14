import requests


response = requests.get('https://ya.ru')
print(response)
print(response.text)

headers = {
    'Accept-Language': 'ru'
}

response = requests.get('http://habr.com', headers=headers)
print(response)
print(response.text)
