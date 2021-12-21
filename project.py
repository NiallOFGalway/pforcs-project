## Author: Niall O Flaherty
## Programming for CyberSecuity - Project
## This project attempts to write a port scanner which will allow the user to enter an IP (and potentially hostname),
## along with either a port (or range of ports). The output will inform the user of open ports on the target address / host

import threading
import socket

