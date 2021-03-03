#!/usr/bin/python3
import socket, time

def banner():
	print("""

|                               |
|===============================|
|-------------------------------|
     [+] By: Anikin Luke [+]
	    Fast|Port|Scanner
	███████╗██████╗ ███████╗
	██╔════╝██╔══██╗██╔════╝
	█████╗  ██████╔╝███████╗
	██╔══╝  ██╔═══╝ ╚════██║
	██║     ██║     ███████║
	╚═╝     ╚═╝     ╚══════╝
	Fast    Port    Scanner
	   (BETA! Version)
|-------------------------------|
|===============================|
|                               |
		""")

banner()
url = input('Enter target: ')
print('===============================')
die = 0

for i in range(1,10001):

	try:
		s = socket.socket()
		s.connect((url, i))
		print(f'[+] port {i} is open!')

	except:
		die+=1

print(f'There are {die} ports are dead! or closed!.')
