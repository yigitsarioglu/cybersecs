# Bu projede ssh ile bağlantı kurulup /etc/passwd dosyası içeriği yazdırıldı
# Ssh connection yapılıp remote command yapıldı

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

for ep in etcpasswd :
	#  print(ep)
	if '/bin/bash' in ep or '/bin/sh' in ep :
		print(ep)


