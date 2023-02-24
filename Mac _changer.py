#created by Sahil maan

import subprocess

mac = input("Please Enter the Required MacAddress : ")
interface = input("please enter the required interface : ")
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

print(mac)
print(interface)
