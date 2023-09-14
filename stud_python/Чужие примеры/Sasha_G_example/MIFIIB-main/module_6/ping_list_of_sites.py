import os


def do_ping_sweep(site_to_ping):
    # ping нужно указывать с параметром -c, чтобы ограничить
    # количество запросов
    response = os.popen(f'ping -c 5 {site_to_ping}')
    res = response.readlines()
    for line in res:
        print(line)
    print("Testing res[]: ")
    for line_res in range(5):
        print(res[line_res]) # здесь res[num] - это одна строка вывода команды ping


list_of_sites = ['mail.ru','ya.ru', 'google.com', 'skillfactory.ru']

for site in list_of_sites:
    print(do_ping_sweep(site))