## Author: Niall O Flaherty
## Programming for CyberSecuity - Project
## This project attempts to write a port scanner which will allow the user to enter an IP (and potentially hostname),
## along with either a port (or range of ports). The output will inform the user of open ports on the target address / host

import threading
import socket
import sys 
import errno 

# Entering the hostname / IP
hostip = input("Please enter the Hostname of IP of target to scan: ")

# Ensure the hostname can be resolved (To an IPv4, see readme.me for code for IPv6 resolution)
hostipresolve = socket.gethostbyname(hostip)

# print(hostipresolve)
# This was used to check that the hostname did actually resolve before going further

startport = input("Please choose first port to scan: ")
endport = input("Please enter the last port to scan: ")
# Choosing the first and last port to scan

print("Scanning remote target for open ports in the range specified", hostipresolve)
# Informing the user the scan has started

try:
  for port in range(int(startport), int(endport)): # Using the range function, inputting the first and last port to scan
      print("Checking if port {} is open".format(port))
      server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket object. AF_INTET = IPv4, SOCK_STREAM = TCP
      server_sock.settimeout(5)
      result = server_sock.connect_ex((hostipresolve, port))
     
      if result == 0:
          print("Port {} is open".format(port))
      
      else:
          print("Port {} is closed".format(port)) # This will inform the user, in English, that the port is closed
          print("Reason:", errno.errorcode[result]) # This will inform the user, technically, why the port is closed
     # server_sock.close()


except socket.error:
  print("Couldn't connect to server")
  sys.exit()