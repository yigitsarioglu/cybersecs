# Linux içerisinde parolaları yazdırmak
# sudo cat /etc/shadow

# Linux içerisinde wordlistlerin olduğu klasörler
#  cd /usr/share/wordlists 
#  wc -l unix_passwords.txt 
# cp unix_passwords.txt /home/kali/Desktop/uygulamalar/python



import subprocess
import crypt


shadow = subprocess.check_output( "cat /etc/shadow" , shell = True).decode()
# print(shadow)

passwd_list = shadow.split("\n")

f = open("unix_passwords.txt" , "r")


for passwd in passwd_list :
	# print(passwd)
	if "kali" in passwd:
		s=passwd.split("$")
		salt = "$" + s[1] + "$" + s[2] + "$" + s[3]
		# print(salt)

		for passwd_try in f:
			tmp_passwd = crypt.crypt ( passwd_try.strip(), salt)
			#print (tmp_passwd)

			if tmp_passwd in passwd:
				print ("Password is : " , passwd_try.strip() )
				break


