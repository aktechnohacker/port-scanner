#!/bin/bash/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py")

#Add a pretty banner



print('''
      
$$$$$$$\                       $$\                                                                      
$$  __$$\                      $$ |                                                                     
$$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\ 
$$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$  _____|$$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  ____/ $$ /  $$ |$$ |  \__| $$ |          \$$$$$$\  $$ /      $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$ |  $$ |$$ |       $$ |$$\        \____$$\ $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |       
$$ |      \$$$$$$  |$$ |       \$$$$  |      $$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__|       \______/ \__|        \____/       \_______/  \_______|\_______|\__|  \__| \_______|\__|
|                                                                                                |
|--------------------------------------------Coded by Ashish Khare-------------------------------|''')

print("\nGithub: https://github.com/aktechnohacker/port-scanner/\n")


print("-" * 50)
print("[+]Scanning Target: "+target)
print("[+]Time started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"port{port} is open")
            s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
