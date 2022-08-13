# 9 AŞAMADA AÇIK KAYNAK İSTİHBARATI (OSINT) NASIL GERÇEKLEŞTİRİLİR?

## 1. IP  Adresi Tespiti ve Coğrafi Konumu

Ip numaralarını tahsis eden kuruluşlar vardır.Bu kuruluşlardan sorumlu olan is ARIN'dir. Kuzey Amerika'ya bakarlar.

- **APNIC - Asya**

- **LACTINC - Latin Amerika**

- **AFRINIC - Afrika**

- **RIPE - Avrupa**

## 2. Shodan & Google Arama Operatörleri

Shodan vb. arama motorları kullanılarak sistemler üzerinde çalışan servisler ve bu servislerin versiyon bilgileri elde edilebilir.

Google arama operatörlerini kullanarak kritik verilere veya dizinlere erişim sağlanabilir.

- **Site**

- **Inurl**

- **Filetpe**

## 3. Sunucu & Web Teknolojilerinin Tespiti

Saldırganlar sunucu işletim sistemi ve üzerinde kullanılan teknolojileri tespit etmeye çalışırlar.

- **[Searchdns.netcraft.com](https://searchdns.netcraft.com/)**

- **[Builtwith.com](https://builtwith.com/)**

## 4.Subdomainlerin Tespit Edilmesi

Saldırganlar hedefe ait alt alan adlarını tespit ederek saldırı yüzeyini genişletmeye çalışır.

- **Google Arama Operatörleri**
- **Virustotal.com**
- **Amass**

## 5. Paylaşımlı Hosting

Bazı web siteleri başka web siteleri ile paylaşımlı sunucularda barındırılabilir. Bunu tespit eden saldırgan, aynı sunucu üzerinde barındırılan başka bir web siteyi hedef alabilir  ve o site üzerinden hedef siteye erişim sağlayabilir.

**Bing Arama Motoru**

**IP : xxx.xxx.xxx.xxx**

## 6. Peki Hedefimiz Bir Şahıs ise?

Sosyal medyalar saldırganlar için en iyi bilgi toplama yöntemidir.

**Twitter.com**

**Facebook.com**

**Instagram.com**

**Pipl.com**


## 7. Arşivler

Saldırganlar , hedef sitenin eski görüntüsüne erişim sağlayabilir ve hassas dizinleri tespit edebilirler.

Haber arşivlerini analiz eden saldırgan, ele geçirmiş olduğu sistemler üzerinden başka sistemlere de erişim sağlayabilir.

örneğin; Marriot Otel Zinciri (2018)

- **Archive.org**

- **Newspaperarchive.com**

## 8. E-posta Adresleri

Saldırganlar sosyal mühendislik saldırıları için hedefe ait e-posta adreslerini tespit edebilir.

Elde edilen e-postalar içerisinde parolası sızdırılmış hesaplar var ise hedef sisteme kaba kuvvet saldırısı yapabilir.

- **[Hunter.io](https://hunter.io/)**

- **[Haveibeenpwned.com](https://haveibeenpwned.com/)**

## 9. Meta Data Analizi

Saldırganlar hedefin internette yayımladığı belgelerdeki meta veri olarak tanımlanan bilgilerden kullanıcı adı, e-posta adresleri ve istemcilerde kullanılan yazılım ve bu yazılımların sürümlerini elde edebilir.

- **Metagoofil**

- **Exiftool**


## DEMO

- 1. IP adresi tespiti : 
  ```$ host google.com ```

- 2. ARIN Sorgulama : arin.net üzerinden ip adres sorgulanır.
- 3. Robtex Sorgulama :  robtex.com üzerinden dnslookup yapılır.
- 4. WHOIS Sorgulame : whois sorgusu yapılır.
```$ whois google.com ```

- 5. Shodan.io üzerinden ip sorgulaması yapılır.
NET : 142.257.187.0/24

- 6. Dork Kullanımı: 
```site: google.com inurl:login```

- 7. Netcraft ile dns sorgulama : Searchdns.netcraft.com üzerinden sorgulanır.

- 8. Subdomainlerin tespiti : virustotal.com üzerinden yapılabilir.

veya google dork kullanılabilir.
örnek: site: google.com.tr -site: https://www.google.com.tr

- 9. Paylaşımlı hosting bulmak: BING arama motoru üzerinden yapılır. örnek sorgu:  ```ip : 10.0.2.5 ```

- 10. archive.org sitesinden eski görüntüye bakmak
- 11. hunter.io ile mail adresleri bulmak.
- 12. Metadata analizi yapılır. 

örnek: site: google.com filetype:pdf

```$exiftool  file.pdf ```