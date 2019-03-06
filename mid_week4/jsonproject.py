import csv
file = open('jsonsearchproject.csv', newline='')
reader = csv.DictReader(file)

query = input('Choose fiscal year, start date, area, asset type, or planning status: ')

years = {}
dates = {}
areas = {}
assettypes = {}
status = {}

for row in reader:
    if query == 'fiscal year':
        x = row['fiscal_year']
        if x not in years:
            years[x] = 1
        else:
            years[x] += 1

    if query == 'start date':
        x = row['start_date']
        if x not in dates:
            dates[x] = 1
        else:
            dates[x] += 1

    if query == 'area':
        x = row['area']
        if x not in areas:
            areas[x] = 1
        else:
            areas[x] += 1

    if query == 'asset type':
        x = row['asset_type']
        if x not in assettypes:
            assettypes[x] = 1
        else:
            assettypes[x] += 1

    if query == 'planning status':
        x = row['status']
        if x not in status:
            status[x] = 1
        else:
            status[x] += 1

if query == 'fiscal year':
    print(years)
elif query == 'start date':
    print(dates)
elif query == 'area':
    print(areas)
elif query == 'asset type':
    print(assettypes)
elif query == 'planning status':
    print(status)
else:
    print('Please type a valid option')


