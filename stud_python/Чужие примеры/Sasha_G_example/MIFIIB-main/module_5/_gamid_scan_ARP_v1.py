import scapy.all as scapy
import argparse

# creating the instance of a class
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', dest='ip_arg', help='Type ip address here')
args = parser.parse_args()
ip = args.ip_arg

arp_req = scapy.ARP(pdst=ip)
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
packet = broadcast/arp_req
# this part doesn't work (sending the packages)
good, bad = scapy.srp(packet, timeout=1)
print(good.summary())
print('*' * 25)
# !!! I have found the result finally. After fighting with installing different versions of python, scapy, launching
# scapy from the root, using sudo I found it. Scapy was installed in PyCharm, the side (terminal) installations
# # didn't help. All I needed to do was to run the script using the correct version of python:
#  sudo python3.9 _gamid_scan_ARP_v1.py -i 10.0.2.0/24
# Begin emission:
# Finished sending 256 packets.
# ***
# Received 3 packets, got 3 answers, remaining 253 packets
# Ether / ARP who has 10.0.2.2 says 10.0.2.16 ==> Ether / ARP is at 52:54:00:12:35:02 says 10.0.2.2 / Padding
# Ether / ARP who has 10.0.2.3 says 10.0.2.16 ==> Ether / ARP is at 52:54:00:12:35:03 says 10.0.2.3 / Padding
# Ether / ARP who has 10.0.2.4 says 10.0.2.16 ==> Ether / ARP is at 52:54:00:12:35:04 says 10.0.2.4 / Padding

# Network 10.0.2.0 - NAT
# Network 192.168.56.0 - VirtualNetwork

#  module_5 % sudo python3 _gamid_scan_ARP_v1.py -i 192.168.1.0/24
# WARNING: No IPv4 address found on en5 !
# WARNING: No IPv4 address found on ap1 !
# WARNING: more No IPv4 address found on awdl0 !
# Begin emission:
# Finished sending 256 packets.
# ..*.*.................................................................................................................................................................................................................
# Received 214 packets, got 2 answers, remaining 254 packets
# Ether / ARP who has 192.168.1.1 says 192.168.1.179 ==> Ether / ARP is at 0c:ef:af:d2:5a:82 says 192.168.1.1
# Ether / ARP who has 192.168.1.2 says 192.168.1.179 ==> Ether / ARP is at f8:f0:82:ae:a8:88 says 192.168.1.2 / Padding
# None


# print('*' * 25, "Output: ")
# this part works well
# print("Packet summary: ", packet.summary())
# print("Packet show: ", packet.show())
# scapy.arping(ip)

# module_5 % sudo python3 _gamid_scan_ARP_v1.py -i 192.168.1.1/24
# WARNING: No IPv4 address found on en5 !
# WARNING: No IPv4 address found on ap1 !
# WARNING: more No IPv4 address found on awdl0 !
# WARNING: More than one possible route for Net("192.168.1.1/24")
# WARNING: More than one possible route for Net("192.168.1.1/24")
# Ether / ARP who has Net("192.168.1.1/24") says 192.168.1.179