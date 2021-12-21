## Author: Niall O Flaherty
## Programming for CyberSecuity - Project
## This project attempts to write a port scanner which will allow the user to enter an IP (and potentially hostname),
## along with either a port (or range of ports). The output will inform the user of open ports on the target address / host

import threading
import socket

# Entering the hostname / IP
hostip = input("Please enter the Hostname of IP of target to scan: ")

# Ensure the hostname can be resolved (To an IPv4, see readme.me for code for IPv6 resolution)
hostipresolve = socket.gethostbyname(hostip)

# print(hostipresolve)
# This was used to check that the hostname did actually resolve before going further

startport = input("Please choose first port to scan: ")
endport = input("Please enter the last port to scan: ")
# Choosing the first and last port to scan

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if startport in range(0, 65535):
        if endport in range(0, 65535):
            for i in range(startport, endport):
                result = sock.connect_ex((hostipresolve, i))
                if(result == 0) :
                    print("Port %d: OPEN") % (i)
                else:
                    print("Port %d: CLOSED") % (i)
                sock.close()
