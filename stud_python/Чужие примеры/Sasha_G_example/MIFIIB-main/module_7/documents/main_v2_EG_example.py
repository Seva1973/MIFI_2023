import json
import os


import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def root():
    return HTMLResponse("<h1>Hello Scaner</h1> <br> <b><u>/scan :</u></b>  <br><br> <b><u>/sendhttp :</u></b> <br>")


@app.get('/scan')
async def scan(ip, num_of_hosts: int = 0):
    print(f'ip {ip} num {num_of_hosts}')
    ip_parts = ip.split('.')
    print(ip_parts)
    answer = f'Result ping {ip} with num {num_of_hosts} \n'
    for host in range(num_of_hosts):
        network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
        scanned_ip = network_ip + str(int(ip_parts[3]) + host)
        response = os.popen(f'ping  -c 2 {scanned_ip} ')
        print(f'{scanned_ip}')
        res = response.readlines()
        answer += f"[#] Result of scanning: {scanned_ip} [#]\n{res[2]} "
        print(f"[#] Result of scanning: {scanned_ip} [#]\n{res[2]}", end='\n\n')

    return {"ip": ip,
            "num_of_hosts": num_of_hosts,
            "answer": answer}


@app.get('/sendhttp')
async def http(target: str, method: str = 'GET', headers=None, payload=None):
    print('sendhttp')
    print(f"{target} {method}")
    print(f'Headers: {headers}')

    headers_dict = dict()
    if headers:
        list_of_headers = headers.split(' ')
        print(list_of_headers)
        for a in list_of_headers:
            s = a.split(':')
            header_name = s[0]
            header_value = s[1]
            headers_dict[header_name] = header_value

        print(headers_dict)
    if method == "GET":
        print(headers_dict)
        response = requests.get(target, headers=headers_dict)
    elif method == "POST":
        response = requests.post(target, headers=headers_dict, data=payload)
    print(f"[#] Response status code: {response.status_code}\n")
    print(f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n")
    return {"status": response.status_code,
            "headers": json.dumps(dict(response.headers), indent=4, sort_keys=True)}