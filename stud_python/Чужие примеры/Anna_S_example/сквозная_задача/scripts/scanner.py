import os
import requests
import json
import platform


def do_ping_sweep(ip, num_of_host):
    """
    Ping sweep function
    :param ip: ip address
    :param num_of_host: number of host to sweep
    """
    ip_parts = ip.split('.')
    network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    scanned_ip = network_ip + str(int(ip_parts[3]) + num_of_host)
    if platform.system() == 'Windows':
        response = os.popen(f'ping {scanned_ip}')
    else:
        response = os.popen(f'ping -c 1 {scanned_ip}')
    res = [line.strip() for line in response.readlines()]
    return {scanned_ip: list(filter(None, res))}


def sent_http_request(target, method, headers_dict=None, payload=None):
    """
    Sending http request function
    :param target: target URL
    :param method: type of method - POST or GET
    :param headers_dict: headers of requests
    :param payload: payload
    """
    response = None
    if method == "GET":
        response = requests.get(target, headers=headers_dict)
    elif method == "POST":
        response = requests.post(target, headers=headers_dict, data=payload)
    return {'Response status code': response.status_code,
            'Response headers': {json.dumps(dict(response.headers), indent=4, sort_keys=True)},
            'Response content': response.text}
