#                                           Plan
# sudo ifconfig eth0 down
# sudo ifconfig eth0 hw ether 08:00:27:25:05:f0 => Note: original MAC was 08:00:27:25:05:f9
# sudo ifconfig eth0 up => Note: the IP accress is changes every cycle of down/up of the interface
# *************************************************************************************************************
# Here, all the tasks require sudo to complete, however, we can save the script and call it from terminal using
# sudo (no one can see the password) this way: $ sudo python3 mac_address_changer.py
import subprocess

mac = input("Enter the MAC address here --> ")
inter = input("Enter the interface, whose MAC addreass we are changing --> ")
subprocess.call("ifconfig " + inter + " down", shell=True)
subprocess.call("ifconfig " + inter + " hw ether " + mac, shell=True)
subprocess.call("ifconfig " + inter + " up", shell=True)
subprocess.call("ifconfig " + inter, shell=True)
