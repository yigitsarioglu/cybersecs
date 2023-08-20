from scapy.all import *

# sudo komutu ile çalıştırılır 
# ornegin sudo python basic_sniffer.py komutu ile çalıştırılır..
# ping 8.8.8.8 ile komut satırında bir pingleme yapılır, diğer terminalde ise bu program çalıştırılabilir

sniff ( prn = lambda x: x.summary(), timeout= 5 , iface= 'eth0') # 5 saniye boyunca eth0 interface'ini dinler