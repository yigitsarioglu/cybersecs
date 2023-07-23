# Scans all ports

# nmap -sS 10.0.2.6 kodunun yaptığı işlevi yapar


import socket

# s = socket.socket ( socket.AF_INET , socket.SOCK_STREAM)

ip = "10.0.2.6"



for port in range (1,65535) :

	try:
		s = socket.socket ( socket.AF_INET , socket.SOCK_STREAM)
		s.connect((ip,port))
		print( str(port), " is open")
		
	except Exception as e:
		#print( str(port), " is closed")
		pass

	finally:
		s.close()