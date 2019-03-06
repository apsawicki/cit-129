import csv
file = open('pgh311Abbrev.csv', newline='')
reader = csv.DictReader(file)

# numCent_Northside = 0
# numSS_Flats = 0
# numTroy_Hill = 0
# numBanksville = 0
# numEast_Hills = 0
# numMount_Washington = 0
# numBluff = 0
# numMiddle_Hill = 0
# numNorth_Oakland = 0
# numCent_Bus_Dist = 0
# numSpring_Hill_City_View = 0
# numBrighton = 0
# numMarshall = 0
# numLawrenceville = 0
# numWindgap = 0
# numBrookline = 0
# numBeechview = 0
# numPerry_N = 0
# numCarrick = 0
# numE_Allegheny = 0
# numBloomfield = 0
# numSheraden = 0
#
# for row in reader:
#     if row['NEIGHBORHOOD'] == 'Central Northside':
#         numCent_Northside = numCent_Northside + 1
#     if row['NEIGHBORHOOD'] == 'South Side Flats':
#         numSS_Flats = numSS_Flats + 1
#     if row['NEIGHBORHOOD'] == 'Troy Hill':
#         numTroy_Hill = numTroy_Hill + 1
#     if row['NEIGHBORHOOD'] == 'Banksville':
#         numBanksville = numBanksville + 1
#     if row['NEIGHBORHOOD'] == 'East Hills':
#         numEast_Hills = numEast_Hills + 1
#     if row['NEIGHBORHOOD'] == 'Mount Washington':
#         numMount_Washington = numMount_Washington + 1
#     if row['NEIGHBORHOOD'] == 'Bluff':
#         numBluff = numBluff + 1
#     if row['NEIGHBORHOOD'] == 'Middle Hill':
#         numMiddle_Hill = numMiddle_Hill + 1
#     if row['NEIGHBORHOOD'] == 'North Oakland':
#         numNorth_Oakland = numNorth_Oakland + 1
#     if row['NEIGHBORHOOD'] == 'Central Business District':
#         numCent_Bus_Dist = numCent_Bus_Dist + 1
#     if row['NEIGHBORHOOD'] == 'Spring Hill-City View':
#         numSpring_Hill_City_View = numSpring_Hill_City_View + 1
#     if row['NEIGHBORHOOD'] == 'Brighton Heights':
#         numBrighton = numBrighton + 1
#     if row['NEIGHBORHOOD'] == 'Marshall-Shadeland':
#         numMarshall = numMarshall + 1
#     if row['NEIGHBORHOOD'] == 'Lower Lawrenceville':
#         numLawrenceville = numLawrenceville + 1
#     if row['NEIGHBORHOOD'] == 'Windgap':
#         numWindgap = numWindgap + 1
#     if row['NEIGHBORHOOD'] == 'Brookline':
#         numBrookline = numBrookline + 1
#     if row['NEIGHBORHOOD'] == 'Beechview':
#         numBeechview = numBeechview + 1
#     if row['NEIGHBORHOOD'] == 'Perry North':
#         numPerry_N = numPerry_N + 1
#     if row['NEIGHBORHOOD'] == 'Carrick':
#         numCarrick = numCarrick + 1
#     if row['NEIGHBORHOOD'] == 'East Allegheny':
#         numE_Allegheny = numE_Allegheny + 1
#     if row['NEIGHBORHOOD'] == 'Bloomfield':
#         numBloomfield = numBloomfield + 1
#     if row['NEIGHBORHOOD'] == 'Sheraden':
#         numSheraden = numSheraden + 1
#
# file.close()
#
# print('Number of 311 reports in each neighborhood:')
# print('Cent. Northside: ', numCent_Northside)
# print('S.S. Flats: ', numSS_Flats)
# print('Troy Hill: ', numTroy_Hill)
# print('Banksville: ', numBanksville)
# print('East Hills: ', numEast_Hills)
# print('Mount Washington: ', numMount_Washington)
# print('Bluff: ', numBluff)
# print('Middle Hill: ', numMiddle_Hill)
# print('North Oakland: ', numNorth_Oakland)
# print('Cent Bus Dist: ', numCent_Bus_Dist)
# print('Spring Hill City View: ', numSpring_Hill_City_View)
# print('Brighton: ', numBrighton)
# print('Marshall: ', numMarshall)
# print('Lawrenceville: ', numLawrenceville)
# print('Windgap: ', numWindgap)
# print('Brookline: ', numBrookline)
# print('Beechview: ', numBeechview)
# print('Perry N.: ', numPerry_N)
# print('Carrick: ', numCarrick)
# print('E. Allegheny: ', numE_Allegheny)
# print('Bloomfield: ', numBloomfield)
# print('Sheraden: ', numSheraden)

neighborhoods = {}

# looked at Xiaohong-Chen's code for the counter
for row in reader:
    x = row['NEIGHBORHOOD']
    if x not in neighborhoods:
        neighborhoods[x] = 1
    else:
        neighborhoods[x] += 1

print(neighborhoods)

