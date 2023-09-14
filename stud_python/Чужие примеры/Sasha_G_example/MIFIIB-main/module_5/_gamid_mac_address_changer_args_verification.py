#                                           Plan
# sudo ifconfig eth0 down
# sudo ifconfig eth0 hw ether 08:00:27:25:05:f0 => Note: original MAC was 08:00:27:25:05:f9
# sudo ifconfig eth0 up => Note: the IP address is changes every cycle of down/up of the interface
# *************************************************************************************************************
# here, all the tasks require sudo to complete, however, we can save the script and call it from terminal using
# sudo (no one can see the password) this way:
# $ sudo python3 mac_address_changer_argparse.py -i eth0 -m 08:00:27:25:05:f6 (-i as interface, -m as new MAC)
# this modification allows to choose interface and the new MAC.
import subprocess
import argparse
import re

# creating the instance of a class
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', dest='inter_arg', help='Type interface name here')
parser.add_argument('-m', '--macaddr', dest='mac_arg', help='Type new MAC address here')
args = parser.parse_args()
print("The values of our arguments: ", args)
print()

args.inter_arg
args.mac_arg

inter = args.inter_arg
mac = args.mac_arg

# This list is used to validate the interface (check if it corresponds the once available in the system)
interfaces_list = ['lo', 'eth0', 'eth1', 'docker0']


def is_valid_mac(str) :
    # regular expression
    regex = (
            "^([0-9A-Fa-f]{2}[:-])" + "{5}([0-9A-Fa-f]{2})|" + "([0-9a-fA-F]{4}\\." + "[0-9a-fA-F]{4}\\." + "[0-9a-fA-F]{4})$")
    match = re.compile(regex)
    if str is None :
        return False
    if re.search(match, str) :
        return True
    else :
        return False


if (inter in interfaces_list) and is_valid_mac(mac) :
    print("Now we are turning the " + inter + " interface off...")
    subprocess.call("ifconfig " + inter + " down", shell=True)
    print()
    print("For the selected interface - " + inter + " we are changing the MAC address to " + mac + " ...")
    subprocess.call("ifconfig " + inter + " hw ether " + mac, shell=True)
    print()
    print("Now we are turning the " + inter + " interface on...")
    subprocess.call("ifconfig " + inter + " up", shell=True)
    print()
    print("The interface " + inter + " has new MAC address - " + mac)
    print()
    print("Running ipconfig for our interface: \n")
    subprocess.call("ifconfig " + inter, shell=True)
else :
    print("Given string is a not a valid interface or valid MAC address!")

# Д/З - ввести проверку на достоверность введённого интерфейса и мак адреса
# Используем Regular Expression для проверки соответствия MAC адреса верному формату
# import re
# def is_valid(str):
# #regural expression
#   regex = ("^([0-9A-Fa-f]{2}[:-])" +"{5}([0-9A-Fa-f]{2})|" +"([0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4})$")
#   match = re.compile(regex)
#   if (str == None):
#     return False
#   if(re.search(match, str)):
#     return True
#   else:
#     return False
# input_string = input("Enter the MAC address: ")
# if(is_valid(input_string)):
#     print("Given string is valid MAC address")
# else:
#     print("Given string is a not valid MAC adress")
