# Python subprocess kullanarak cihazın MAC adresini değiştirme

import random
import subprocess
import re

charList = [ "0", "1" , "2" , "3" , "4" , "5" , "6" ,"7", "8" ,"9" ,"A" ,"B" , "C" ,"D" ,"E" ,"F"]

newMac = ""
 
for i in range (12) :
	newMac = newMac + random.choice (charList)

print (newMac)




# TERMİNAL İfconfig çalıştırma sorgusu
ifconfigResult = subprocess.check_output ("ifconfig eth0" ,shell=True).decode()
print(ifconfigResult)


# REGEX ile mac adresini seçip almak
oldMac = re.search ("ether(.+) ", ifconfigResult).group().split(" ")[1]
print (oldMac)


# Regex başka bir yöntem
#oldMac = re.search ("ether(.*?)txqueuelen", ifconfigResult).group(1).strip()
#print (oldMac)




#Mac adresini değiştirme, shell komutları çalıştırararak

subprocess.check_output ("ifconfig eth0 down" , shell="True")
subprocess.check_output("ifconfig eth0 hw ether ") +newMac, shell ="True" )
subprocess.check_output("ifconfig eth0 up", shell=True)


# Son olarak Eski ve yeni mac adresini görüntüleme
print ("Old Mac : ", oldMac)
print ("New Mac : ", newMac)