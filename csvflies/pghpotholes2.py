import csv
file = open('pgh311Abbrev.csv', newline='')
reader = csv.DictReader(file)
line_reader = file.readlines()

req_origin = []
centralCount = {}
for x in line_reader:
    pghfile = x.split(',')[6]
    req_origin.append(pghfile)

for y in range(0, 34):
    query = req_origin[y]
    if query not in centralCount:
        centralCount[query] = 1
    else:
        centralCount[query] += 1

print('The amount of pot hole reports per territory', end='\n')
print(centralCount, end='\n')
print('The more the number of reports may correlate with the condition of the roads within each territory')
