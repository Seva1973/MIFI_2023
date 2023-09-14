import os

# ping нужно указывать с параметром -c, чтобы ограничить
# количество запросов
command = "ping -c 10 skillfactory.ru"

response = os.popen(command)
res = response.readlines()
for line in res:
    # print(line.encode('cp1251').decode('cp866')) для Windows среды
    print(line)