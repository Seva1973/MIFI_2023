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
    print(existing_IP_addresses)
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
        your_ip = input("Enter your starting IP: ")
        num_of_hosts_to_scan = int(input("Enter the number of hosts to scan: "))
        # передаём стартовый IP и количество хостов для пинга
        ping_list = do_ping_sweep(your_ip, num_of_hosts_to_scan)
        self.wfile.write(f"Successfully pinged IP addresses: {ping_list}".encode())

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
# ---------> Работает вариант SCAN!!!
# запустил скрипт, стартовал сервер, вывод виден в терминале и Postman выдаёт разультат.
# вот только он сканирует закодированный адрес и число хостов: ping_list = do_ping_sweep("192.168.1.115", 2), а
# хотелось бы передавать в запросе GET. Разбираюсь.

"""
$ python3 main_first_dockerized.py
127.0.0.1 - - [12/Mar/2023 23:56:45] "GET /?ip=192.168.1.115&num_scanned_hosts=5 HTTP/1.1" 200 -
192.168.1.115

**********************************************************************

Full output of ping:  ['PING 192.168.1.115 (192.168.1.115): 56 data bytes\n', '\n', '--- 192.168.1.115 ping statistics ---\n', '1 packets transmitted, 0 packets received, 100.0% packet loss\n']
[#] Result of scanning 192.168.1.115
PING 192.168.1.115 (192.168.1.115): 56 data bytes

--- 192.168.1.115 ping statistics ---

1 packets transmitted, 0 packets received, 100.0% packet loss


This IP doesn't belong to the network

**********************************************************************

**********************************************************************

Full output of ping:  ['PING 192.168.1.116 (192.168.1.116): 56 data bytes\n', '64 bytes from 192.168.1.116: icmp_seq=0 ttl=64 time=2.363 ms\n', '\n', '--- 192.168.1.116 ping statistics ---\n', '1 packets transmitted, 1 packets received, 0.0% packet loss\n', 'round-trip min/avg/max/stddev = 2.363/2.363/2.363/0.000 ms\n']
[#] Result of scanning 192.168.1.116
PING 192.168.1.116 (192.168.1.116): 56 data bytes



--- 192.168.1.116 ping statistics ---


This IP belongs to the network

**********************************************************************
['192.168.1.116']

"""