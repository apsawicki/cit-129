from bs4 import BeautifulSoup
import requests

url = 'https://pokemondb.net/pokedex/national'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
typefinder = soup.findAll(class_='itype grass')
statfinder = soup.findAll(class_='cell-num')

pokemon = {
    'names': [],
    'types': [],
    'id': []
}

stats = []

for items in statfinder:
    son = items.findChild
    print(son)
# number = 1
# for items in typefinder:
#     pokemon[number] = items.text
#     number += 1
#     dad = items.find_parent("small")
#     uncle = dad.previous_sibling
#     twonduncle = uncle.previous_sibling
#     threeuncle = twonduncle.previous_sibling
#     idnum = threeuncle.previous_sibling
#     pokemon['names'].append(twonduncle.text)
#     pokemon['id'].append(idnum.text)
#     pokemon['types'].append(dad.text)

# print(pokemon['names'])
# print(pokemon['types'])
# print(pokemon['id'])
# infocard-lg-data text-muted

