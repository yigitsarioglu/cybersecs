# Working website founder (WoURL)
# Ping websites and finds the working url

import subprocess

start_number = 1770
end_number = 1850

# https://www.xyzsportsgiris2.xyz/
# base_url = "xyzsportsgiris"


def ping_website(host):
    try:
        # Windows için ping komutunu çalıştırır
        result = subprocess.run(["ping", "-n", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"Working website found: {host}")
            return True  # Ping başarılı
    except Exception as e:
        print(f"Ping error for {host}: {e}")
    return False  # Ping başarısız

def main():
    base_url = "selcuksportshd"
    
    domain = ".xyz"
    working_urls = []

    for i in range(start_number, end_number):  # Bu aralıktaki url leri tarayacak
        host = f"{base_url}{i}{domain}"
        print(f"Checking: {host}")  # Kontrol edilen URL'yi ekrana yaz
        if ping_website(host):
            working_urls.append(host)

    # Çalışır durumda olan URL'leri yazdır
    print("\nWorking URLs:")
    for url in working_urls:
        print(url)

if __name__ == "__main__":
    main()
