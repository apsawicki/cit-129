import json
pokemon = {}
pokemon['list'] = ['hello alex', 'hello again']
pokemon['names'] = ['name boi']
pokemon['test'] = [' ']


with open("pokemon.txt", "w+") as f:
    f.write(json.dumps(pokemon))

