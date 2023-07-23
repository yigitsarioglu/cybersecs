# Sublime text run etmek için CTRL +B kısayolu kullanılır
# Ping Icmp üzerinden gerçekleştirilir
# Ping kullanarak host discovery aracı yapılması
# Scapy kütüphanesi kullanılmıştır.

from scapy.all import *

ipList = []

ip = IP()
icmp = ICMP()

pingPckt = ip/icmp

addr = "10.0.2."

for i in range (256) :
	pingPckt[IP].dst = addr + str(i)
	#print (pingPckt[IP].dst )
	# sr1 komutu paket gönderme ve alma için kullanılır
	response = sr1 (pingPckt, timeout = 0.5 , verbose = False)
	# print(response)

	if(response) :
		print(pingPckt[IP].dst , " is up")
		ipList.append(pingPckt[IP].dst)
	else :
		pass

print ("Açık olan ip listesi : " , ipList)

