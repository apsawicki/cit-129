import csv
import json

file = json.load(open('jsoncriteria.txt', newline=''))
reader = csv.DictReader(file)
file_two = open('jsonsearchproject.csv', newline='')
reader_two = csv.DictReader(file_two)

# Dictionaries
year = {}
date = {}
status = {}
area = {}
asset = {}
data_dict = {}
new_dict = {}

# asking the question
row_select = input('Choose either year, date, area, asset, status: ')

# counter and data for data_dict
for row in reader_two:
    identity = row['id']
    data_dict[identity] = row
    if row_select == 'year':
        value = row['fiscal_year']
        if value not in year:
            year[value] = 1
        else:
            year[value] += 1
            new_dict = data_dict.copy()
    if row_select == 'date':
        value = row['start_date']
        if value not in year:
            date[value] = 1
        else:
            date[value] += 1
    if row_select == 'area':
        value = row['area']
        if value not in year:
            area[value] = 1
        else:
            area[value] += 1
    if row_select == 'asset':
        value = row['asset_type']
        if value not in year:
            asset[value] = 1
        else:
            asset[value] += 1
    if row_select == 'status':
        value = row['status']
        if value not in year:
            status[value] = 1
        else:
            status[value] += 1
# make option 6 the one that shows the data through the data dictionary maybe???



# printing
if row_select == 'year':
    print(year, end='\n')
elif row_select == 'date':
    print(date, end='\n')
elif row_select == 'area':
    print(area, end='\n')
elif row_select == 'asset':
    print(asset, end='\n')
elif row_select == 'status':
    print(status, end='\n')
else:
    print('ERROR')
# print(new_dict)

choice = input('Which key would you like to sort by: ')
for x in new_dict.keys():
    if data_dict[x]['fiscal_year'] != choice:
        del data_dict[x]
print(data_dict)
