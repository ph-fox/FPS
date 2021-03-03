#!/usr/bin/python3
import socket, time, os

try:
	from IPy import IP
	from colorama import Fore, Style
except ImportError:
	os.system("pip3 install colorama")
	os.system("pip3 install IPy")


	
def banner():
	print("""
|                               |
|===============================|
|-------------------------------|
     [+] By: Anikin Luke [+]
	    Fast|Port|hScanner
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

f = Fore
r = f.RED
b = f.BLUE
y = f.YELLOW
g = f.GREEN
st = Style.BRIGHT

def check(target):
	try:
		IP(target)
		return(target)

	except ValueError:
		return socket.gethostbyname(target)

def vinfo(s):
	return s.recv(1024)

print(f'{st}{r}┌──({y}Enter㉿Target-IP-or-Domain{r})-[{b}~/FPS{r}]')
ui = input(f"{r}└─>->>{g} ")

target = check(ui)
print('===============================')
die = 0

print('scanning target...\n')
for i in range(1,10001):

	try:
		s = socket.socket()
		s.settimeout(.1)
		s.connect((target, i))

		try:
			data = vinfo(s)
			data2 = data.decode().strip('\n')
			print(f"""|=========================|
|[+] port {i} is open!   |
|[$] {data2} |
|=========================|""")

		except:
			print(f"""|=========================|
|[+] port {i} is open!  |
|=========================|""")

	except:
		die+=1
		if(i == 100):
			print(f'[scanning port {i}  above..]')
		elif(i == 500):
			print(f'[scanning port {i}  above..]')
		elif(i == 1000):
			print(f'[scanning port {i} above..]')
			#ui = input(f'continue scanning above {i} port? (y/n):')
			#if ui == 'y':
			#	pass
			#	print(f'[scanning port {i} above..]')
			#else:
			#	break

		elif(i == 2000):
			print(f'[scanning port {i} above..]')
			#ui = input(f'continue scanning above {i} port? (y/n):')
			#if ui == 'y':
			#	pass
			#	print(f'[scanning port {i} above..]')
			#else:
			#	break

		elif(i == 4000):
			print(f'[scanning port {i} above..]')
			#ui = input(f'continue scanning above {i} port? (y/n):')
			#if ui == 'y':
			#	pass
			#	print(f'[scanning port {i} above..]')
			#else:
			#	break


		elif(i == 7000):
			print(f'[scanning port {i} above..]')
			#ui = input(f'continue scanning above {i} port? (y/n):')
			#if ui == 'y':
			#	pass
			#	print(f'[scanning port {i} above..]')
			#else:
			#	break


		elif(i == 10000):
			print(f"""
<<================================>>
[!] port {i} MAX Scan Reach!!!..
[*]Scan Complete!.
<<================================>>""")

if die == 10000:
	print(f'ALL {die} PORTs ARE CLOSE!')
	print(f'Target has not open ports')
else:
	print(f'There are {die} ports are dead! or closed!.')
