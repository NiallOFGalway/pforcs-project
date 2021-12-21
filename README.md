# Programming for CyberSecurity - Project - Niall O Flaherty 
Port Scanner using Python

This project aims to create a program that will allow the user to input an IP address and port number to check if the post is open on the target device. As there are 1024 (0 - 1023) known ports and a total of 65535 ports in range, this project will attempt to allow the user to enter a port range and scan the range.

Furthermore, this project will attempt to use modules available in Python to allow the user to scan not just by IP, but also by host-name, by way of DNS resolution.

Research has shown that this project is quite a common one for students world-wide and there is an abundance of knowledge / code online. Therefore, this project does not aim to re-invent the wheel or write previously unknown code, but more-so to gain an understanding of the Python language, the available code out there and to be able to honestly say "This is how it works, this actually makes sense to me".

Initial research shows that scanning ports can be time consuming, especially if a large range of ports are to be scanned. This time delay can be over-come using threading.


**WHAT IS THREADING?**

*"Threading is a complex topic, but it can be broken down and conceptualized as a methodology where we can tell the computer to do another task if the processor is experiencing idle time. In the case of port scanning, we are spending a lot of time just waiting on the response from the server. While we are waiting, we can do something else. That is what threading is used for"*
- https://www.geeksforgeeks.org/threaded-port-scanner-using-sockets-in-python/


Further research regarding Port Scanners using Python refer to 'Sockets' and using the 'Socket' module in Python. Therefore, before investigatin further on how to actually start coding to write a port scanner, it is imperative that the student gains an understanding to the terminology of the technoloy / modules available, which is the aim of this project.


**WHAT IS A SOCKET?**

A basic networking definition of a Socket is: IP Address + Port = Socket. Instantly, this makes sense as to perform a port scan, you need both a target IP address and a port to scan.

*"Python's standard library consists of various built-in modules that support interprocess communication and networking. The network access is available at two levels. The 'socket' module defines how server and client machines can communicate at hardware level using socket endpoints on top of the operating system"*
- https://www.knowledgehut.com/tutorials/python-tutorial/python-socket-module


## Writing the Code ##
1) Import Threading
.Explained Above

2) Import Sockets
.Explained Above

3) Ensure host can be resolved to IP
NOTE: The code used in this project will only resolve to an IPv4 Address. If IPv6 resolution is required, use the following code: gethostbyname()
Reference: https://pythontic.com/modules/socket/gethostbyname



## REFERECES

https://www.geeksforgeeks.org/threaded-port-scanner-using-sockets-in-python/

https://www.knowledgehut.com/tutorials/python-tutorial/python-socket-module

https://pythontic.com/modules/socket/gethostbyname
