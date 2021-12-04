import socket
import sys
import time
import threading
from build.scanning import *
import os, sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

usage = "Usage: Pscann.py <IP-ADDRESS> <option(s)>"
if len(sys.argv) == 1 or sys.argv[1] == "--help" or len(sys.argv) == 2:
	fileHelp = open("help.txt","r")
	design_banner()
	print(fileHelp.read())
	sys.exit()
else:
	target = socket.gethostbyname(sys.argv[1])
	option = sys.argv[2]
	print(banner())
	try:
		mode(target, option)
	except:
		print("[*] Something went wrong.")
	sys.exit()