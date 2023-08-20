from scapy.all import *

def sniffPckt (pkt) :
	pkt.show()



# Sniffing metodu, eğer bir ping işlemi yapılırsa duracaktır
# örneğin komut satırından ping 8.8.8.8 yazıp run ederseniz sniffing işlemi duracak
def start_sniff() :
	scapy_sniff = sniff ( prn= sniffPckt, timeout=50 , iface ='eth0' , stop_filter = lambda x:x.haslayer(ICMP) )

	wrpcap( 'dinleme.pcap' , scapy_sniff)  # pcap dosyasına yazdırmak için, böylece wireshark ile analizi yaparız


def start_read():
	scapy_cap = rdpcap('dinleme.pcap')
	ip_list = []

	for pckt in scapy_cap :
		if IP in pckt:
			if pckt[IP].src not in ip_list:
				ip_list.append(pckt[IP].src)
		else:
			pckt.show()

	print(ip_list)	

		


## Buradan sonrası komut satırından kullanıcıyı yönlendirmek içindir


print( """ 1: sniff
		   2: read
	""")



choice = input ( ">>")


if (choice == "1") :
	start_sniff()

elif (choice == "2"):
	start_read()

else:
	print("Hatalı giriş...")
