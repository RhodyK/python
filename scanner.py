#!/bin/python

#usage: python3 scanner.py <ip>
import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #hostname to ipv4 just in case
else:
    print("Invalid argument usage")
    print("Syntax: python3 scanner.py <ip>")

print("-" * 50)
print("Scanning target "+target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)
#attempt scan on ports 50-85 @ target IP
try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns error indicator - 0 = open 1 = closed
        if result == 0:
            print("Port {} is open".format(port))
            print("-"*50)
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connet to server.")
    sys.exit()
