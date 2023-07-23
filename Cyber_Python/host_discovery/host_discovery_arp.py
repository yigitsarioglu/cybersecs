# Scapy kütüphanesi kullanarak, arp istekleri göndererek, çevredeki makineler(aynı ağdaki) tespit edilir
from scapy.all import *

eth = Ether()
arp = ARP ()

eth.dst = "ff:ff:ff:ff:ff:ff"

arp.pdst = "10.0.2.1/24"

bckPkt = eth/arp


#layer 2 paket gönderimi

ans , unans =srp (bckPkt, timeout = 5)

#ans.summary()
#print("#" *30)
#unans.summary()


for snd,rcv in ans :
	rcv.show()
	print ( rcv.src , " : ", rcv.psrc)