# запуск программы производится из терминала:
# % sudo python3 _gamid_scan.py
import scapy.all as scapy
import argparse

# creating the instance of a class
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', dest='ip_arg', help='Type ip address here')
args = parser.parse_args()
ip = args.ip_arg


scapy.arping(ip)


# *******************************************************************************ip
# Результат:
# ... module_5 % sudo python3 _gamid_scan.py
# Password:
# WARNING: No IPv4 address found on en5 !
# WARNING: No IPv4 address found on ap1 !
# WARNING: more No IPv4 address found on awdl0 !
# Begin emission:
# Finished sending 256 packets.
# ***
# Received 3 packets, got 3 answers, remaining 253 packets
#   0c:ef:af:d2:5a:82 unknown 192.168.1.1
#   f8:f0:82:ae:a8:88 unknown 192.168.1.2
#   e0:2b:e9:46:e7:68 unknown 192.168.1.103