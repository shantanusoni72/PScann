import socket
import sys
import time
import threading
import pyfiglet
bS = pyfiglet.figlet_format("Pscann")
print(bS)
def scanPorts(port):
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	final = con.connect_ex((target,port))
	if final:
		pass
	else:
		print("Port {} is open".format(port))
	con.close()
usage = "Usage: Pscann.py <IP-ADDRESS> <STARTING-PORT> <ENDING-PORT>"
target = socket.gethostbyname(sys.argv[1])
startingPort = 0
endingPort = 0
if sys.argv[2] == "-sF":
	endingPort = 1000
if sys.argv[2] == "-sH":
	endingPort = 500
if sys.argv[2] == "-sB":
	endingPort = 100
if sys.argv[2] == "--help":
	fileHelp = open("help.txt","r")
	print(fileHelp.read())
if len(sys.argv) != 3:
    print(usage)
else:
	for port in range(startingPort,endingPort+1):
		Thread = threading.Thread(target = scanPorts,args=(port,))
		Thread.start();