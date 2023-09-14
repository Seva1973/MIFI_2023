Создание файла requirement.txt:
$ pip freeze > requirement.txt

Dockerfile:
FROM python:3.9
WORKDIR /code
LABEL Author=A.Ganitev
LABEL module=7.10
COPY ./requirements.txt /code/requirements.txt
# folder /code belongs to the inner structure of this Docker container
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y iputils-ping
COPY ./app /code/app
EXPOSE 3009
ENTRYPOINT ["python3"]
CMD ["app/main.py"]
# CMD ["app/main.py", "--host", "0.0.0.0", "--port", "3009"] # здесь надо было именно через / указать путь до main.py
# во вложенной директории app
**************************************************************
            Запуск самой программы (до Докера):
1. Переходим в папку (module_7), где лежит app/main.py и запускаем:
$ python3 app/main.py (app - это для указания субдиректории, где лежит main.py, можно из неё запустить)
2. Запускаем Postman и отправлям GET request
            Создание контейнера в Docker, запуск программ из контейнера и отправка запросов GET и POST
Создание Docker image:
$ module_7 % docker build -t scanner_postman .
# Запуск: docker run scanner_postman
Запуск с привязкой порта: docker run -p 3009:3009 scanner_postman (с проброской портов 3009)
            Формат запроса (request из Postmant API передаём как словарь):
GET: {"ip":"192.168.1.1","num_scanned_hosts":"3"}
GET/POST: {"target":"https://ya.ru", "method": "GET"}

Note: Also make sure your process is listening on host 0.0.0.0 (instead of localhost).
Container's localhost is not the same as your host's localhost
***************************************************************
# Обновление, надо убрать доп.символы в переменной Temp:ValueError: invalid literal for int() with base 10: '115\\n'
# Запуск Debagger-а для такой программы с API:
# 1. Отмечаем breakpoints, запускаем дебаггер
# 2. В Postman отправляем запрос и смотрим в окне дебаггера...

        # пришлосъ пойти на такую хитрость с replace(), терерь сканер работает! Символ '\\n' был удалён из 4-го октета.
        ip_parts[3] = ip_parts[3].replace('\\n', '')
        print(ip_parts[3])
        network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
        ping = "ping -c 1 "
        time1 = datetime.datetime.now()
        # for ip in range(115, 118) :  # так отрабатывает, ниже вариант даёт ошибку:
            #     for ip in range(int(ip_parts[3]), int(ip_parts[3])+int(5)) :
            #                     ^^^^^^^^^^^^^^^^
            # ValueError: invalid literal for int() with base 10: '1\\n\\n'
            # проблема связана со строкой выше: content = self.rfile.read(length), где добаляюся символы 'b', \n.
            # надо их удалить, работаю...
*******************************************************************
Note: when the Python script is modified, the Docker image has to be rebuilt.
Also, check the IP, the terminal is linked when the ping is working, it's 172.17.0.1 - this is the address of the
system of the container.
*******************************************************************
При запуске сканера (GET запрос) на указанный IP, возникала ошибка: /bin/sh: 1: ping: not found
Почитал и установил дополнительные пакеты в Dockerfile:
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y iputils-ping
*******************************************************************
GET request: запуск сканера с двумя аргументами, парсим payload = json.loads(temp), в
который передаём запрос в API в виде:
{"ip":"192.168.1.177", "num_scaned_hosts":"3"}
Тут тоже пришлось удалять дополнительные форматирующие файлы:
'{"ip":"192.168.1.177","num_scanned_hosts":"3"}\\n\\n'
        # удаление добавленных '\\n' символов из строки GET request:
        temp = temp.replace('\\n', '')
        # Отправить GET запрос на API, а в теле запроса указать:
        # {"ip":"192.168.1.1","num_scanned_hosts":"3"}
        # переменная payload получает словарь {} в виде: {"ip":"192.168.1.1","num_scanned_hosts":"3"}
        # из Postman, теперь по ключам можно передавать значения в основную функцию:
        payload = json.loads(temp)
        scan_sweep_result = do_ping_sweep(payload["ip"], payload["num_scanned_hosts"])
*******************************************************************
POST request: теперь вместо закодированной строки в do_POST() хочется
разобраться, как парсится строка и как передавать её в запросе Postman-а

        # Отправить POST запрос на API, а в теле запроса указать:
        # {"target":"https://ya.ru", "method": "GET"}
        # переменная payload получает словарь {} в виде: {"target":"https://ya.ru", "method": "GET"}
        # из Postman, теперь по ключам можно передавать значения в основную функцию:
        payload = json.loads(temp)
        http_request_response = send_http_request(payload["target"], payload["method"])

Парсим json в таком виде, т.к. POST request передаст payload как словарь {}, и в дальнейшем надо будет
вытащить все символы, для передачи в send_http_request()
"В Postman мы передаём строку так:
“target”: “www.ya.ru”, “method”:“GET” или
{“target”: “www.ya.ru”, “method”:“GET”} или
target:www.ya.ru, method:GET?"
Лучше передавать как {“target”: “www.ya.ru”, “method”:“GET”} . Потому что в таком случае Вы можете использовать библиотеку json. {} вот эти скобочки делают из обычной строки словарь. В котором {"ключ": "значение"}. И Питон умеет с такой структурой работать. Если передадите просто строкой без {}, уже придется самому писать обработку этой строки с нуля.
Вы правы, в любом случае к Вам придет тип string, но внутри него будут уже {}, а питоновская библиотека json умеет работать с такой структурой и для нее это уже не строка, а словарь.
Если же передаете
“target”: “www.ya.ru”, “method”:“GET”
То это также будет просто строка, но Вы уже не сможете использовать библиотеку json. Придется костылями обрабатывать всю эту строку постепенно. Убирать символы, строки и т.д.
По итогу, если работать с json, то у Вас строка temp станет словарем, из которого Вы уже сможете вытаскивать значения по ключу. Ну скажем с помощью json Вы конвертировали строку temp в словарь dict, и теперь dict["target"] - это в аккурат будет строка "www.ya.ru", а dict["method] - строка "GET".
В случае без json вы в temp должны в итоге получить list (список), который ввыглядит как-то так:
["www.ya.ru", "GET"]
И тогда temp[0] - это ваш таргет, temp[1] - это метод.
Дальше сможете спокойно в свою функцию передавать либо temp[0] и temp[1], либо dict["target"] и dict["method"].
*******************************************************************
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
$ python3 main.py
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




