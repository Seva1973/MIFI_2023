import requests

#response = requests.get("http://info.cern.ch/")
#print (f"Код ответа сервера: {response.status_code}")
#вызовет "код ответа 200"

#response = requests.get("http://info.cern.ch/")
#headers = response.headers
#print(headers["content-type"])
# вызовет "text/html


#response = requests.get("http://info.cern.ch/")
#headers = response.headers
#print(headers) #Просто вывести заголовок
# вызовет такое {'Date': 'Fri, 24 Feb 2023 10:43:41 GMT', 'Server': 
#'Apache', 'Last-Modified': 'Wed, 05 Feb 2014 16:00:31 GMT', 'ETag':
# '"286-4f1aadb3105c0"', 'Accept-Ranges': 'bytes', 'Content-Length': 
#'646', 'Connection': 'close', 'Content-Type': 'text/html'}

#headers = {"Accept-Language": "ru"}
#response = requests.get("http://habr.com/", headers=headers)
#print(response.text)
# выводит html код с руссими заголовками

import json
import requests


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
        f"[#] Response content:\n {response.text}"
    )


target = str(input("Target:"))
method = str(input("Method (GET|POST):"))
headers = list(input("Headers (name1:value1 name2:value2 ...)").split())
if method == "POST":
    payload = str(input("Payload:"))

sent_http_request(target, method, headers, payload)
