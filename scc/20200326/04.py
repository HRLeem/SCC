import requests
from bs4 import BeautifulSoup

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
print(r)
rjson = r.json()
print(rjson['RealtimeCityAir']['row'])
big = rjson['RealtimeCityAir']['row']
for item in big :
    if 70 > item['IDEX_MVL'] > 0:
        print(item['MSRSTE_NM'], item['IDEX_MVL'] ,item['IDEX_NM'] )
