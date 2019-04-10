from bs4 import BeautifulSoup
import requests

# personal website

file = open('C:/Users/apsaw/Documents/Sublime/mealdbapi.html')
html = file.read()
soup = BeautifulSoup(html, 'html.parser')
l = soup.findAll(class_='secheader')
for item in l:
    print(item.text)

# allegheny county property record database

url = 'http://www2.county.allegheny.pa.us/RealEstate/GeneralInfo.aspx?ParcelID=0160C00272000000&SearchType=2&SearchStreet=N%20JACKSON&SearchNum=105&SearchMuni=803'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
ele = soup.find('span', id='BasicInfo1_lblOwner')
print(ele.text)
