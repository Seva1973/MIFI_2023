import os

def do_ping_sweep(site):
    response = os.popen(f'ping {site}') 
    res = response.readlines()
    for line in res: 
          print(line.encode('cp1251').decode('cp866'))

list_of_sites = ['ya.ru', 'google.com', 'skillfactory.ru']

for site in list_of_sites : 
	do_ping_sweep(site)
