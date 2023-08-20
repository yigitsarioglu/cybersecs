# Bu proje belirtilen Url deki title,content ve time alanlarını beautifulsoup kütüphanesi kullanarak web kazıma yapar, yani filtreleyip gösterir..

import requests

from bs4 import BeautifulSoup


url = "https://stackoverflow.com/questions/tagged/python-requests"   # herhangi bir web sayfası belirleyebilirsiniz
response = requests.get(url)
#print ( response.text )


parser = BeautifulSoup ( response.text , 'html.parser')

questions = parser.find_all ( "div" , {"class" : "s-post-summary"} )

for q in questions:
	#print(q)
	
	# title alanlarını ayıklar
	title = q.find ('h3', {"class": "s-post-summary--content-title"})
	print(title.text.strip() )

	# content alanları ayıklar
	content = q.find ( 'div' , {"class" : "s-post-summary--content-excerpt"})
	print (content.text.strip() )


	# time degerini ayıklama
	time = q.find ('span' , {"class" : "relativetime"} )
	print(time['title'])

	print("------------")






##########################

# Spanleri bulup gösterir
#spans = parser.find_all("span")

#for s in spans :
#	print(s.text)

#######################



