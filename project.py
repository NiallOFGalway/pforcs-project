import socket
import threading

from queue import Queue 

print_lock = threading.Lock()
queue = Queue() # Defining the Queue for threader

# Entering the hostname / IP
targetip = input("Please enter the Hostname of IP of target to scan: ")

# Ensure the hostname can be resolved (To an IPv4, see readme.me for code for IPv6 resolution)
hostipresolve = socket.gethostbyname(targetip)

# Choosing the first and last port to scan
startport = input("Please choose first port to scan: ")
endport = input("Please enter the last port to scan: ")


def portscanner(port):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket object. AF_INTET = IPv4, SOCK_STREAM = TCP
    try:
        con = server_sock.connect((targetip,port)) # Try to connect to the target (targetip) and port (port) - The ports to scan will be defined later
        with print_lock:
            print ("Port",port,"is open")

        con.close() # Close the connection when complete
    except: # If the port is open, just pass... no point in wasting screen space ie. "Port is closed"
        pass

def threader():
    while True:
        portstoscan = queue.get()
        portscanner(portstoscan)
        queue.task_done() # When the task is complete, empty out the Q

for x in range(int(startport), int(endport)): # Using the range function, inputting the first and last port to scan
    t = threading.Thread(target=threader) # Create threader. Gets ports from the portscanner
    t.daemon = True 
    t.start()

for portstoscan in range(int(startport), int(endport)): # Using the range function, inputting the first and last port to scan
    queue.put(portstoscan)

queue.join()
    
