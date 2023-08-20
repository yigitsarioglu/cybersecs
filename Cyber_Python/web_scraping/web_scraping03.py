# Client Side web scraping 
# javascript
# https://curlconverter.com/python/

# exploit-db sitesini web kazıma yapıyoruz..
import requests
import requests

cookies = {
    'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1692565897982%2Cregion:%27TR%27}',
    '_ga': 'GA1.3.1990008123.1692565898',
    '_gid': 'GA1.3.1584709430.1692565898',
    '_gat': '1',
    '_ga_N0K6XSDCRJ': 'GS1.3.1692565898.1.1.1692565968.60.0.0',
    'XSRF-TOKEN': 'eyJpdiI6ImlRK2NqODhteVhIdDBiQ011ZnYxZkE9PSIsInZhbHVlIjoiOFwvUWRRMVZWY2owNmIyY1wvVzhtdWRnU2RpWStNU1BcL0JUdjNsdkE5a3FIRFF4Y1JuRTVHdTZcL2FMajNmYVBmZ28iLCJtYWMiOiJlNzk3NDdlZGVhNTVjZDAwNTU5OGVkMGQ3NTk3OTJkZGJmYjViMmRhMzJiMWFjNDg2YjFmMmQxNzQwYmE5ZTJlIn0%3D',
    'exploit_database_session': 'eyJpdiI6IlwvUFNDNzNZYnF4dzVtWDAxOUk4dFl3PT0iLCJ2YWx1ZSI6ImZhQU5zWlM5RFYzbzhnb2UwYzQ1ZVNVZ2tJbHBkUUFqamNQWXhCQWVtODg5cG53V0M5bVBUbWxUXC84N1lTT3NIIiwibWFjIjoiNDIyYTFhNTI0NWIwZmFhNmI2NTkzZDE2Nzc3ZDgwMjQzYmUzOWIxMGIzMTg4YjYyMTRiYmMyN2MxMDQ5MzNlNCJ9',
}

headers = {
    'authority': 'www.exploit-db.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1692565897982%2Cregion:%27TR%27}; _ga=GA1.3.1990008123.1692565898; _gid=GA1.3.1584709430.1692565898; _gat=1; _ga_N0K6XSDCRJ=GS1.3.1692565898.1.1.1692565968.60.0.0; XSRF-TOKEN=eyJpdiI6ImlRK2NqODhteVhIdDBiQ011ZnYxZkE9PSIsInZhbHVlIjoiOFwvUWRRMVZWY2owNmIyY1wvVzhtdWRnU2RpWStNU1BcL0JUdjNsdkE5a3FIRFF4Y1JuRTVHdTZcL2FMajNmYVBmZ28iLCJtYWMiOiJlNzk3NDdlZGVhNTVjZDAwNTU5OGVkMGQ3NTk3OTJkZGJmYjViMmRhMzJiMWFjNDg2YjFmMmQxNzQwYmE5ZTJlIn0%3D; exploit_database_session=eyJpdiI6IlwvUFNDNzNZYnF4dzVtWDAxOUk4dFl3PT0iLCJ2YWx1ZSI6ImZhQU5zWlM5RFYzbzhnb2UwYzQ1ZVNVZ2tJbHBkUUFqamNQWXhCQWVtODg5cG53V0M5bVBUbWxUXC84N1lTT3NIIiwibWFjIjoiNDIyYTFhNTI0NWIwZmFhNmI2NTkzZDE2Nzc3ZDgwMjQzYmUzOWIxMGIzMTg4YjYyMTRiYmMyN2MxMDQ5MzNlNCJ9',
    'referer': 'https://www.exploit-db.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'draw': '1',
    'columns[0][data]': 'date_published',
    'columns[0][name]': 'date_published',
    'columns[0][searchable]': 'true',
    'columns[0][orderable]': 'true',
    'columns[0][search][value]': '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': 'download',
    'columns[1][name]': 'download',
    'columns[1][searchable]': 'false',
    'columns[1][orderable]': 'false',
    'columns[1][search][value]': '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': 'application_md5',
    'columns[2][name]': 'application_md5',
    'columns[2][searchable]': 'true',
    'columns[2][orderable]': 'false',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': 'verified',
    'columns[3][name]': 'verified',
    'columns[3][searchable]': 'true',
    'columns[3][orderable]': 'false',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'columns[4][data]': 'description',
    'columns[4][name]': 'description',
    'columns[4][searchable]': 'true',
    'columns[4][orderable]': 'false',
    'columns[4][search][value]': '',
    'columns[4][search][regex]': 'false',
    'columns[5][data]': 'type_id',
    'columns[5][name]': 'type_id',
    'columns[5][searchable]': 'true',
    'columns[5][orderable]': 'false',
    'columns[5][search][value]': '',
    'columns[5][search][regex]': 'false',
    'columns[6][data]': 'platform_id',
    'columns[6][name]': 'platform_id',
    'columns[6][searchable]': 'true',
    'columns[6][orderable]': 'false',
    'columns[6][search][value]': '',
    'columns[6][search][regex]': 'false',
    'columns[7][data]': 'author_id',
    'columns[7][name]': 'author_id',
    'columns[7][searchable]': 'false',
    'columns[7][orderable]': 'false',
    'columns[7][search][value]': '',
    'columns[7][search][regex]': 'false',
    'columns[8][data]': 'code',
    'columns[8][name]': 'code.code',
    'columns[8][searchable]': 'true',
    'columns[8][orderable]': 'true',
    'columns[8][search][value]': '',
    'columns[8][search][regex]': 'false',
    'columns[9][data]': 'id',
    'columns[9][name]': 'id',
    'columns[9][searchable]': 'false',
    'columns[9][orderable]': 'true',
    'columns[9][search][value]': '',
    'columns[9][search][regex]': 'false',
    'order[0][column]': '9',
    'order[0][dir]': 'desc',
    'start': '0',
    'length': '15',
    'search[value]': '',
    'search[regex]': 'false',
    'author': '',
    'port': '',
    'type': '',
    'tag': '',
    'platform': '',
    '_': '1692566002044',
}

response = requests.get('https://www.exploit-db.com/', params=params, cookies=cookies, headers=headers)


# print(response.text) # json formatta bilgiye ulaştık



###################################

jsonData  = response.json()

exploits = jsonData['data']

for exploit in exploits :

	id = exploit['id']
	title = exploit ['description'][1]
	type = exploit['type']['display']
	platform  = exploit['platform']['platform']
	author = exploit ['author'] ['name']
	link = "https://www.exploit-db.com/" + exploit['download'].split("\"")[1]


	print (id,title,type,platform,author,link)
