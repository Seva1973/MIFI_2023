# coding=utf-8
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import requests
import json

existing_IP_addresses = []


def do_ping_sweep(ip, num_scanned_hosts) :
    global existing_IP_addresses
    ip_parts = ip.split('.')
    for host in range(num_scanned_hosts):
        network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
        scanned_ip = network_ip + str(int(ip_parts[3]) + host)
        # c – Количество отправляемых пакетов, устанавливаем = 1, если больше, то будет больше строк вывода
        # тем не менее, иногда про одном пинге и про плохой связи
        # можно потерять пакет, посланый реальному хосту в сети
        # решение: пересканировать или изменить на 2, 3 или больше.
        response = os.popen(f'ping -c 1 {scanned_ip}')
        res = response.readlines()
        print('\n' + '*' * 70)
        print("\nFull output of ping: ", res)
        print(f"[#] Result of scanning {scanned_ip}\n{res[0]}\n{res[2]}\n{res[3]}", end='\n\n')
        # починил! здесь надо разделять условные операторы используя any
        # важно: для пинга телефона, в оный нужно залогиниться, чтобы был успешный пинг
        if any(("ttl=" in word for word in res) or ("TTL=" in word for word in res)) :
            print("This IP belongs to the network\n")
            existing_IP_addresses += [scanned_ip]
            print('*' * 70)
        else :
            print(f"This IP doesn't belong to the network\n")
            print('*' * 70)
    return existing_IP_addresses


def send_http_request(target: str, method: str = "GET", headers=None, payload=None) :
    headers_dict = dict()
    if headers :
        for header in headers :
            header_name = header.split(':')[0]
            header_value = header.split(':')[1 :]
            headers_dict[header_name] = ':'.join(header_value)
        print(headers_dict)
    if method == "GET" :
        response = requests.get(target, headers=headers_dict)
    elif method == "POST" :
        response = requests.post(target, headers=headers_dict, data=payload)
    print(
        f"[#] Response status code: {response.status_code}\n"
        f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"[#] Response content:\n {response.text}"
    )
    return {"Status": response.status_code, "Headers": json.dumps(dict(response.headers), indent=4, sort_keys=True)}


# Обработка запросов
class ServiceHandler(BaseHTTPRequestHandler) :
    # Устанавливаем параметры заголовков для ответа
    def set_headers(self) :
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        length = int(self.headers["Content-Length"])
        content = self.rfile.read(length)
        # The b literal in front of the string literal means that the given string is in bytes' format.
        # The b literal converts string into byte format. In this format bytes are actual data and string
        # is an abstraction.
        temp = str(content).strip('b\'')
        self.end_headers()
        return temp

    # Обрабатываем GET запросы
    def do_GET(self) :
        temp = self.set_headers()
        print(temp)
        # передаём стартовый IP и количество хостов для пинга
        ping_list = do_ping_sweep(ip="192.168.1.1", num_scanned_hosts="5")
        self.wfile.write(f"The list of successfully pinged IP addresses: {ping_list}".encode())

    # Обрабатываем POST запросы
    def do_POST(self) :
        temp = self.set_headers()
        print(temp)
        # Если получаем POST запрос:
        # self.wfile.write((f"Complete! Doubled number is: {numberx2}").encode())


# Запускаем HTTP сервер
server = HTTPServer(('0.0.0.0', 3009), ServiceHandler)
server.serve_forever()

# Documentation: https://docs.python.org/3/library/http.server.html
# вызвал сервер командой:
# python -m http.server
# ответ:
# Serving HTTP on :: port 8000 (http://[::]:8000/) ...
# надо разобраться, как передавать GET запрос через Postman. Оригинальная программа работала так:
# python3 main_start.py scan -i 192.168.1.1 -n 10

# попытался запустить без HTTPсервера сам скрипт, но без argparse,
# я не понимаю, как передать аргументы. Исследую.
