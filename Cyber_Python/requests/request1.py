import requests


url = "https://github.com/"


header= { 'user-agent':'yigitsarioglu/1.1.1' }

# Get isteği gönderilmesi
#r = requests.get(url, headers=header, allow_redirects=False , timeout=2)

# Dönen status_code gösterilmesi
#print (r.status_code)  

#print(r.headers)

#print ( r.headers.get('Date'))

# Tüm web sayfasının gösterilmesi
#print(r.text)

try:
    # Temel olarak request atma kodu, timeout ve redirects parametrelerine değerleri siz vereceksiniz
    r = requests.get(url, headers=header, allow_redirects=False , timeout=0.1)

    print (r.status_code)

    print(r.headers)

    print ( r.headers.get('Date'))

except Exception as e:

    print(e)

    pass

    