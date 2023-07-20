# Login.php sayfasına Post atıp Login olma
import requests


url = "http://10.10.10.128/dvwa/login.php"

data = {'username': 'admin' , 'password':'password' , 'Login':'Login' }



try:
    # Post atılması
    r = requests.post(url, data = data , allow_redirects=True )

    print (r.status_code)

    print(r.text)

except Exception as e:

    print(e)

    pass