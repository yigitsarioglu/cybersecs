# Nmap host discovery, port taraması ,servis taraması , script kullanımı


import nmap


nm = nmap.PortScanner()

ip_range = "10.0.2.1/24"

nm.scan(ip_range, arguments="-sn")

# Host taraması yapılır, açıp IP bulunur
for host in nm.all_hosts() :
	print(host)


ip_list = ' '.join(nm.all_hosts() )

print(ip_list)




#Servis taraması
nm.scan (ip_list, arguments='-sV')
# print(nm.scaninfo() )



http_ip_list = []
http_port_list = []

# TCP olanları ayıklar, onların içerisinde de "http" port olanlarını ayıklar.. bunların versiyonlarını,port numaralarını ve isimlerini de print eder
for ip in nm.all_hosts() :
	if "tcp" in nm[ip]:
		print ( nm[ip]['tcp'].keys() )
		print("---"*20)

		for port in nm[ip]['tcp'].keys() :
			#print( nm[ip]['tcp'][port] )

			if ( nm[ip]['tcp'][port]['name'] == "http" ) :
				name = nm[ip]['tcp'][port]['name']
				product = nm[ip]['tcp'][port]['product']
				version = nm[ip]['tcp'][port]['version']
				print (ip, port , name, product,version)

				if ip not in http_ip_list :
					http_ip_list.append(ip)
				if port not in http_port_list:
					http_port_list.append(port)


print (http_ip_list)
print (http_port_list)