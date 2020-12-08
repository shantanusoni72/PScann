import socket
import sys
import time
import threading
import pyfiglet
bS = pyfiglet.figlet_format("Pscann")
print(bS)
print("				Code by: Shaan453")
fileName = ""
lineOfList = "Port scan report \n "
def scanPorts(port):
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	final = con.connect_ex((target,port))
	if final:
		pass
	else:
		portSet = "Port {} is open".format(port)
		print(portSet)
		if sys.argv[-2] == "-o":
			file = open(sys.argv[-1]+".txt","a")
			file.write(portSet+"\n")
			file.close()
		else:
			pass
	con.close()

def saveFile(fileName):
	try:
		save = open(fileName,"a")
	except:
		print("File not found")
	save.write(lineOfList)
	save.close()

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
else:
	pass

if sys.argv[2] == "--help":
	fileHelp = open("help.txt","r")
	print(fileHelp.read())
else:
	pass

for port in range(startingPort,endingPort+1):
	Thread = threading.Thread(target = scanPorts,args=(port,))
	Thread.start()