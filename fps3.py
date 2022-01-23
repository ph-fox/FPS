import socket, os, time, threading, sys
from IPy import IP

def identify(ip):
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)

def scan(ip, port):
	try:
		s=socket.socket()
		s.settimeout(.1)
		s.connect((ip, port))
		try:
			x = s.recv(1024)
			x=x.decode().strip('\n')
		except:
			x=' '
		os.system(f'echo {port} >> open_ports.txt')
		#print(f"\r [{port}] |({x})   "+' '*len(str(port)))

	except:
		pass

def thread(host):
	for port in range(1,65535):
		threading.Thread(target=scan, kwargs={'ip':host,'port':port}).start()
		sys.stdout.write(f"\r             "+" "*len(str(port)))
		sys.stdout.write(f'\r scanning {port}   ')
	op = open('open_ports.txt')
	o_p = op.read().splitlines()
	print('\r                        ')
	for port in o_p:
		print(f'\r {port}')
	print('\r=======================\n Done!                ')
	op.close()

if __name__=="__main__":
	try:
		host = sys.argv[1]
		os.system('del open_ports.txt')
		thread(host)
	except:
		print(f"By: Anikin Luke\nUsage:\n python3 {os.path.basename(__file__)} <host>")
