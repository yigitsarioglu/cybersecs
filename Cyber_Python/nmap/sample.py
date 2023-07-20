# This code does port scan using nmap python library.
# You should first install nmap with this command : pip install python-nmap 
import nmap

scanner = nmap.PortScanner()

ip = "10.0.2.5"

# Versiyon taraması yapmak için sV kullanırız
scanner.scan(ip,'0-100','-sV')


# Scaninfo bilgisi verir
# print ( scanner.scaninfo() )


# Bir yerin ayakta olup olmadığını kontrol eder
print ( "host", ip , ": ", scanner[ip].state())


# Hangi protokoller kullanılmış
print("Protocols : " , scanner[ip].all_protocols())


# Tcp üzerinde hangi portların tarandığı dictionary ye konur
print ( "Open ports : " , scanner [ip]['tcp'].keys())


# Belirli bir port hakkında bilgi almak için
print ( "Port 21 : " , scanner[ip]['tcp'][21] )


# For döngüsü kullanarak tüm portları taratmak
#for port in scanner [ip]['tcp'].keys() :
	#print ( scanner[ip]['tcp'][port]  )



# For döngüsü kullanarak tüm portları taratmak
for port in scanner [ip]['tcp'].keys() :
	#print ( scanner[ip]['tcp'][port]  )
	portNumber = scanner[ip]['tcp'][port]
	name = scanner[ip]['tcp'][port]['name']
	product = scanner[ip]['tcp'][port]['product']
	version = scanner[ip]['tcp'][port]['version']
	print(port ,name,product,version)