import requests
import json

url = "https://www.themealdb.com/api/json/v1/1/latest.php"
req = requests.get(url)

# happiness testing

# if int(req.status_code) == 200:
#     print('200!')
# else:
#     print('not 200')

# QUESTION: are the latest meals more healthy or unhealthy?

api = json.loads(req.text)
data_dict = {}
data_dict['categories'] = []
data_dict['meal_names'] = []
counter = {}

# Counter, meal name, meal category

for x in range(0, 10):
    data_dict['categories'].append(api['meals'][x]['strCategory'])
    data_dict['meal_names'].append(api['meals'][x]['strMeal'])

for x in range(0, 10):
    value = data_dict['categories'][x]
    if value not in counter:
        counter[value] = 1
    else:
        counter[value] += 1

# Prints

print('                                   MEAL NAMES:CATEGORIES')
for x in range(0, 10):
    print(data_dict['meal_names'][x], end=': ')
    print(data_dict['categories'][x], end='\n')
print('                       PERCENTAGES OF FOOD CATEGORIES IN THE 10 LATEST MEALS')
for x in counter:
    # if x == desert then make it print unhealthy percentage of deserts, else print healthy percentages with others categories
    print(x, end=': ')
    print(counter[x] / 10 * 100, '%', end='\n')

print(data_dict['categories'])
