import os
import argparse
from typing import TextIO
import requests
import json

"""Syntax:
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(name or flags...[, action][, nargs][, const]
                    [, default][, type][, choices][, required]
                    [, help][, metavar][, dest])"""
existing_IP_addresses = []


def do_ping_sweep(ip, num_of_host) :
    global existing_IP_addresses
    ip_parts = ip.split('.')
    network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    scanned_ip = network_ip + str(int(ip_parts[3]) + num_of_host)
    # c – Количество отправляемых пакетов, устанавливаем = 1, если больше, то будет больше строк вывода
    # w - Устанавливает время ожидания (если есть необходимость в использовании
    response = os.popen(f'ping -c 1 {scanned_ip}')
    res = response.readlines()
    print('\n' + '*' * 70)
    print("\nFull output of ping: ", res)
    # всего вывод списка res состоит из 4 строк, негативный пинг:
    # ['PING 192.168.1.156 (192.168.1.156): 56 data bytes\n',
    # '\n',
    # '--- 192.168.1.156 ping statistics ---\n',
    # '1 packets transmitted, 0 packets received, 100.0% packet loss\n']
    # при успешном пинге, строк будет 5, ищем по паттерну "ttl"
    print(f"[#] Result of scanning {scanned_ip}\n{res[0]}\n{res[2]}\n{res[3]}", end='\n\n')

    if any(("ttl=" in word for word in res) or ("TTL=" in word for word in res)):
        print("This IP belongs to the network\n")
        existing_IP_addresses += [scanned_ip]
        print('*' * 70)
    else:
        print(f"This IP doesn't belong to the network\n")
        print('*' * 70)
        return existing_IP_addresses


def sent_http_request(target, method, headers=None, payload=None) :
    headers_dict = dict()
    if headers :
        for header in headers :
            header_name = header.split(':')[0]
            header_value = header.split(':')[1 :]
            headers_dict[header_name] = ':'.join(header_value)
    if method == "GET" :
        response = requests.get(target, headers=headers_dict)
    elif method == "POST" :
        response = requests.post(target, headers=headers_dict, data=payload)
    print(
        f"[#] Response status code: {response.status_code}\n"
        f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"[#] Response content:\n {response.text}"
    )


parser = argparse.ArgumentParser(description='Network scanner')
parser.add_argument('task', choices=['scan', 'sendhttp'], help='Network scan or send HTTP request')
parser.add_argument('-i', '--ip', type=str, help='IP address')
parser.add_argument('-n', '--num_of_hosts', type=int, help='Number of hosts')
parser.add_argument('-t', '--target', type=str, help='Target for http requests')
parser.add_argument('-m', '--method', choices=['GET', 'POST'], help='GET or POST method')
parser.add_argument('-hd', '--headers', nargs='*', type=str, help='Request headers')
parser.add_argument('-p', '--payload', type=str, help='Request headers')

args = parser.parse_args()

if args.task == 'scan' :
    for host_num in range(args.num_of_hosts) :
        do_ping_sweep(args.ip, host_num)
    print('\t\t\tStatistics:')
    print("\nList of existing IP addresses:")
    print(existing_IP_addresses)
    print('*' * 70 + '\n')
else:
    sent_http_request(args.target, args.method, args.headers, args.payload)

# Writing to file
listIP: TextIO
# using "a" as parameter to append and write to the file. If the file doesn't exist - it's being created
with open("list_of_IP_addresses.txt", "a") as listIP :
    # Writing data to a file
    listIP.write(f"The list of IPs found in this session: \n")
    for line in existing_IP_addresses :
        listIP.write(line + '\n')


# ******** All works ********
# Запуск сканера: python3 _network_hosts_scanner_final.py scan -i 192.168.1.1 -n 10
# или с начала пула существующих адресов:
# python3 _network_hosts_scanner_final.py scan -i 192.168.1.110 -n 140
# программа составляет список IP адресов, которые дают ответ по паттерну 'ttl'
# Запуск HTTP запроса: HTTP request to https://google.com:
# python3 _network_hosts_scanner_final.py sendhttp -t https://google.com -m GET -hd Accept-Language:ru

