import csv
file = open('pgh311Abbrev.csv', newline='')
reader = csv.DictReader(file)
line_reader = file.readlines()

req_origin = []
centralCount = 0
for x in line_reader:
    pghfile = x.split(',')[6]
    req_origin.append(pghfile)
    for j in req_origin:
        if j == "Central Northside":
            centralCount = centralCount + 1
print(req_origin)
print(centralCount)

# for row in reader:
#     row['NEIGHBORHOOD'] = 0


# numCallCenter = 0
# numReport2GovIOS = 0
# numReport2GovAndroid = 0
# numWebsite = 0
# numTwitter = 0
# numControlPanel = 0
#
# for row in reader:
#     if row['REQUEST_ORIGIN'] == "Call Center":
#         numCallCenter = numCallCenter +1
#     elif row['REQUEST_ORIGIN'] == "Report2GovIOS":
#         numReport2GovAndroid = numReport2GovAndroid + 1
#     elif row['REQUEST_ORIGIN'] == "Report2GovAndroid":
#         numReport2GovAndroid = numReport2GovAndroid + 1
#     elif row['REQUEST_ORIGIN'] == "Website":
#         numWebsite = numWebsite + 1
#     elif row['REQUEST_ORIGIN'] == "Control Panel":
#         numControlPanel = numControlPanel + 1
#
# print(numControlPanel)
# print(numTwitter)
# print(numWebsite)
# print(numReport2GovAndroid)
# print(numReport2GovIOS)
# print(numCallCenter)
#
