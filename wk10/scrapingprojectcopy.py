from bs4 import BeautifulSoup
import requests

# scrape into a useful format (maybe searching)(put into nicely formatted text file)(html website)

pokemon = []
types = ['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying',
         'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']

print('The types of pokemon are the following:', end='\n')
for x in types:
    print(x, end='\n')
poketype = input('Choose the type of pokemon: ')

url = 'https://pokemondb.net/pokedex/national'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
ele = soup.findAll(class_='infocard-lg-data text-muted')
for items in ele:
    pokemon.append(items.text)

for x in range(0, 809):
    if poketype in pokemon[x]:
        print(pokemon[x])

# p = x.parent
# for child in p.children:
#     print(child.text)
