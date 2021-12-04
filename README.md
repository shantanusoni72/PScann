# PScann
PScann is a network security tool (Port Scanner) for discovering hosts, services and system ports on
a computer network by sending packets and analyzing the responses.

![image](https://user-images.githubusercontent.com/75296055/144709205-8ff6ea7c-db71-4507-95c3-7c0f5f1c0341.png)

**Tech Stack:** Python, Python Networking Modules.

Current version avaiable is 2021.5.3.
### Installation
1. `git clone https://github.com/shaan453/PScann.git`
2. `cd pscann`

### Usage
`python3 pscann.py <ip-address> <option(s)>`

	-sF: 		Full scan. Scan 63000 ports.
	-sH: 		Half scan. Scan 30000 ports.
	-sB: 		Baby scan. Scan 1000 ports.
	--help:		Display help.
