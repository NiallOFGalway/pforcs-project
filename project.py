## Author: Niall O Flaherty
## Programming for CyberSecuity - Project
## This project attempts to write a port scanner which will allow the user to enter an IP (and potentially hostname),
## along with either a port (or range of ports). The output will inform the user of open TCP ports on the target address / host

import threading
import socket

from queue import Queue 

print_lock = threading.Lock()
queue = Queue() # Defining the Queue for threader

# Entering the hostname / IP
targetip = input("Please enter the Hostname or IP (v4) of target to scan: ")

# Ensure the hostname can be resolved (To an IPv4, see readme.me for code for IPv6 resolution)
hostipresolve = socket.gethostbyname(targetip)

# Choosing the first and last port to scan
startport = input("Please choose first TCP port to scan: ")
endport = input("Please enter the last TCP port to scan. Add 1 to your last port ie. if last port is 100, enter 101: ")


def portscanner(port):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket object. AF_INTET = IPv4, SOCK_STREAM = TCP
    try:
        con = server_sock.connect((targetip,port)) # Try to connect to the target (targetip) and port (port) - The ports to scan will be defined later
        with print_lock:
            print ("Port",port,"is open")

        con.close() # Close the connection when complete
    except: # If the port is closed, just pass... no point in wasting screen space ie. "Port is closed"
        pass

def threader():
    while True:
        portstoscan = queue.get()
        portscanner(portstoscan)
        queue.task_done() # When the task is complete, empty out the Q

for x in range(int(startport), int(endport)): # Using the range function, inputting the first and last port to scan
    thread = threading.Thread(target=threader) # Create threader. Gets ports from the portscanner
    thread.daemon = True # Threads are either daemon or non-daemon. This defines the thread as daemon. This means that the thread runs without blocking the main program from exiting.
    thread.start() # This starts the thread after it has been created. This was a 'head scratcher' and I could not get the program to produce any output until I eventually added this line.

for portstoscan in range(int(startport), int(endport)): # Using the range function, inputting the first and last port to scan
    queue.put(portstoscan)

queue.join()