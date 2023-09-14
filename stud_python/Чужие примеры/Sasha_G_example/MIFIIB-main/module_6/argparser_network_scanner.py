import argparse

parser = argparse.ArgumentParser(description="Network scanner")
parser.add_argument("ip", type=str, help="IP address")
parser.add_argument("num_of_hosts", type=int, help="Number of hosts")
args = parser.parse_args()

print(args.ip)

# стартуем в терминале, передаём параметры:
# python3 /Users/alexandrganitev/ProgrammingPython/pythonProject3.9/mifiib_homework/module_6
# python3 argparser_network_scanner.py 192.168.1.0 20