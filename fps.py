#!/usr/bin/python3
import socket, time
from IPy import IP

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
=================================""")

banner()

def check(target):
	try:
		IP(target)
		return(target)

	except ValueError:
		return socket.gethostbyname(target)


ui = input('Enter target: ')
target = check(ui)
print('===============================')
die = 0

print('scanning target...\n')
for i in range(1,10001):

	try:
		s = socket.socket()
		s.settimeout(.1)
		s.connect((target, i))
		print(f"""|=======================|
|[+] port {i} is open!  |
|=======================|""")
	except:
		die+=1
		if(i == 100):
			print(f'\n[scanning port {i}  above..]')
		elif(i == 500):
			print(f'[scanning port {i}  above..]')
		elif(i == 1000):
			print(f'[scanning port {i} above..]')
		elif(i == 5000):
			print(f'[scanning port {i} above..]')
		elif(i == 9000):
			print(f'[scanning port {i} above..]')	
		elif(i == 10000):
			print(f"""
<<================================>>
[!] port {i} MAX Scan Reach!!!..
[*]Scan Complete!.
<<================================>>""")

print(f'There are {die} ports are dead! or closed!.')
