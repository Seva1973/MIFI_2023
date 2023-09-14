import requests


def call_api_ping_sweep(ip: str = '192.168.0.1', count: int = 3):
    """
    Call API ping sweep
    :param ip: ip address
    :param count: number of hosts to ping
    """
    response = requests.get("http://localhost:3000/scan", params={"ip": ip, "count": count})
    print(response.status_code)
    print(response.headers)
    print(response.json())


def call_api_send_http(target: str = 'https://ya.ru', method: str = 'GET',
                       header: str = 'Server', header_value: str = 'HTTP'):
    """
    Call API send http
    :param target: target URL
    :param method: type of method - POST or GET
    :param header: Header type
    :param header_value: Header value
    :return:
    """
    response = requests.post("http://localhost:3000/sendhttp", params={"target": target, "method": method,
                                                                       "header": header, "header_value": header_value})
    print(response.status_code)
    print(response.headers)
    print(response.json())


if __name__ == '__main__':
    print("Run test api calls")
    print("Test API ping sweep (defaults ip=192.168.0.1, count=3)")
    call_api_ping_sweep()
    print("Test API ping sweep (defaults target=https://ya.ru, method=GET, header=Server, header_value=HTTP)")
    call_api_send_http()
