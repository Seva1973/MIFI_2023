#                                           Plan
# sudo ifconfig eth0 down
# sudo ifconfig eth0 hw ether 08:00:27:25:05:f0 => Note: original MAC was 08:00:27:25:05:f9
# sudo ifconfig eth0 up => Note: the IP accress is changes every cycle of down/up of the interface
# *************************************************************************************************************
# Here, all the tasks require sudo to complete, however, we can save the script and call it from terminal using
# sudo (no one can see the password) this way: $ sudo python3 mac_address_changer_script_subprocessFn.py
import subprocess

mac = input("Type your MAC address here --> ")
# The value of mac is a string in a form of 'mac'

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether " + mac, shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
subprocess.call("ifconfig eth0", shell=True)

print("Just for fun, listing of cwd: ")
# cwd listing
subprocess.run(["ls", "-l"])
