import bs4
from bs4 import BeautifulSoup
import requests



url=input("ENter the product url")
#url = "https://www.flipkart.com/dell-ms-116-wired-optical-mouse/p/itmekm2ggehfhfaw?pid=ACCEKM2GZAGFW2TM&lid=LSTACCEKM2GZAGFW2TMF3S8CR&marketplace=FLIPKART&q=mouse&store=search.flipkart.com&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=af2938d4-8684-4f07-97c2-d803f5d2690c.ACCEKM2GZAGFW2TM.SEARCH&ppt=None&ppn=None&ssid=fsj3uaohow0000001627824033651&qH=40203abe6e81ed98"

req = requests.get(url)
soup = bs4.BeautifulSoup(req.text, "html.parser")

# print name from product page
name = soup.find("h1")
for info in name:
    product = info.getText()
    print(info.getText())
    print("---------------")
# print price
price=soup.find('div',{"class":"_30jeq3 _16Jk6d"}).text
print(price)
print("---------------------")
#review
for rv in soup.find_all('div',{"class":"_16PBlm"}):
 bb=rv.get_text()
 print(bb)
 print("------------------")
