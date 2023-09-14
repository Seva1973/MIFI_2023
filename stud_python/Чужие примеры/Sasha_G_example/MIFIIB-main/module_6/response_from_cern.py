import requests

response = requests.get('http://info.cern.ch/')
print("Status code существующего ресурса: ", response.status_code, "\n")
print(response.text)
headers = response.headers
print("Тип содержимого ответа: ", headers["content-type"], "\n")

print("Запрос несуществующего ресурса: ")
response = requests.get('http://info.cern.ch/password.txt')
print(f"Код ответа сервера: {response.status_code}")

print("Смена языка в запросе на сервер: \n")
headers = {"Accept-Language": "ru"}
response = requests.get("http://habr.com/", headers=headers)
print(response.text)