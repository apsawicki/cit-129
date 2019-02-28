import csv
file = open('jail.csv', newline='')
reader = csv.DictReader(file)
numBlack = 0
numWhite = 0
num28YearsOld = 0
targetDate = '2018-01-01'
valWhite = 'W'
valBlack = 'B'


for row in reader:
    if row['date'] == targetDate:
        if int(row['agecurr']) == 28:
            num28YearsOld = num28YearsOld + 1
        if row['race'] == valWhite:
            numWhite = numWhite + 1
        elif row['race'] == valBlack:
            numBlack = numBlack + 1
file.close()
print('total 28 year-olds: ' + str(num28YearsOld))
print('num white inmates: ' + str(numWhite))
print('num black inmates: ' + str(numBlack))
percentBlack = numBlack / (numBlack + numWhite)
print('percent black inmates: ' + str(percentBlack))
