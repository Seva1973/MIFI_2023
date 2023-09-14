"""Использование API:

http://numbersapi.com/<number>/<type>
number — число;
type — тип факта (trivia — факт из жизни, math — математический факт,
date и year — вопрос про дату (в формате MM/DD) и год).
Например, получить факт о 25 октября можно по запросу:

http://numbersapi.com/10/25/date
October 25th is the day in 1760 that George III becomes King of Great Britain."""

import json
import requests


# headers and payload (=None) – необязательные аргументы
def sent_http_request(target, method, headers=None, payload=None):
    headers_dict = dict()

    if headers:
        for header in headers:
            header_name = header.split(":")[0]
            header_value = header.split(":")[1:]
            headers_dict[header_name] = ":".join(header_value)

    if method == "GET":
        response = requests.get(target, headers=headers_dict)
    elif method == "POST":
        response = requests.post(target, headers=headers_dict, data=payload)
    print(
        f"[#] Response status code: {response.status_code}\n"
        f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"[#] Response content: \n {response.text}"
    )


target = str(input("Target: "))
method = str(input("Method (GET|POST):"))
headers = list(input("Headers (name1:value1 name2:value2 ...):").split())
if method == "POST":
    payload = str(input("Payload:"))
# для случая с GET only:
else:
    payload = None

sent_http_request(target, method, headers, payload)

# Target: http://numbersapi.com/
# Method (GET|POST): GET
# Headers (name1:value1 name2:value2 ...): 16/math


"""После того, как код будет запущен, он будет ожидать ввода значений для ряда переменных. 
Для начала вводится значение для target, то есть цели отправки запроса (URL). Далее ожидается 
ввод значения для переменной method, которая определяет тип запроса — POST или GET. Далее идёт 
ввод значения переменной headers, так как подразумевается, что заголовков запроса может быть 
несколько. Каждый заголовок вводится в формате name:value через пробел. После этого введённые 
данные преобразуются в список с помощью метода split(), который по умолчанию разделяет строку 
по пробельным символам. Затем, если в переменную method было передано значение POST, то для 
данного типа запросов в переменной payload указываются данные, которые будут передаваться в 
его теле.

Далее вызывается функция sent_http_request, при этом для функции определены два позиционных 
(то есть обязательных) аргумента target и method, а также два необязательных аргумента headers 
и payload, для которых по умолчанию выставлено значение None."""
