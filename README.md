# Programming for CyberSecurity - Project - Niall O Flaherty 
Port Scanner using Python

This project aims to create a program that will allow the user to input an IP address and port number to check if the post is open on the target device. As there are 1024 (0 - 1023) known ports and a total of 65535 ports in range, this project will attempt to allow the user to enter a port range and scan the range.

Initial research shows that scanning ports can be time consuming, especially if a large range of ports are to be scanned. This time delay can be over-come using threading.

WHAT IS THREADING?
"Threading is a complex topic, but it can be broken down and conceptualized as a methodology where we can tell the computer to do another task if the processor is experiencing idle time. In the case of port scanning, we are spending a lot of time just waiting on the response from the server. While we are waiting, we can do something else. That is what threading is used for"
- https://www.geeksforgeeks.org/threaded-port-scanner-using-sockets-in-python/
