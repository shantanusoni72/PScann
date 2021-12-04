import sys
import socket
import threading
import datetime
import pyfiglet

def design_banner():
    print(pyfiglet.figlet_format("PScann"))

def banner():
	return '-------------------------------------Pcann-2021.5.3-Scan-----------\n'+'-'*41+str(datetime.datetime.now())

def scanning(target, startingPort, endingPort):
    for port in range(startingPort,endingPort+1):
        Thread = threading.Thread(target = scanPorts,args=(target,port,)) 
        Thread.start()

def scanPorts(target,port):
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    final = con.connect_ex((target,port))
    if port == 63000 or port == 30000 or port == 1000:
        pass
    else:
        if final:
            pass
        else:
            portSet = "Port {} is open".format(port)
            print(portSet)
            con.close()

def saveFile(fileName):
    fileName = ""
    lineOfList = "Port scan report \n"

def mode(target, option):
    startingPort = 0
    endingPort = 0
    if option == "-sF":
        endingPort = 63000
    if option == "-sH":
        endingPort = 30000
    if option == "-sB":
        endingPort = 1000
    scanning(target, startingPort, endingPort)