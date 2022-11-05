#build port scanner

import sys
import socket
from datetime import datetime 
from unittest import result

#define our target 
if len(sys.argv) == 2:
	 target = socket.gethostbyname(sys.argv[1])# translate hostname to IPV4

else: 
	print("invalid amount of argument:") 
	print("syntax:python3 scanner.py ")

print ("-" * 50) 
print ("scanning target "+target) 
print ("time started:" +str(datetime.now())) 
print ("-" * 50)

try:
	 for port in range(55,65): #can set any range(1,65535)
	 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) socket.setdefaulttimeout(1) result = s.connect_ex((target,port)) #return an error indicator 
	if result == 0: print("port {} is open".format(port)) s.close() 
except KeyboardInterrupt: 
	print("\n exiting program") 
	sys.exit() 
except socket.gaierror: 
	print("hostname colud not be resolved.") 
	sys.exit() 
except socket.error: 
	print("couldn't connect to server") 
	sys.exit()
