import csv
import json

file = json.load(open('jsoncriteria.txt', newline=''))
file_two = open('jsonsearchproject.csv', newline='')
reader = csv.DictReader(file)
reader_two = csv.DictReader(file_two)


list = []
new_list = []

for row in reader_two:
    list.append(row)


def main():
    row_select = input('Choose a row from either fiscal_year, start_date, area, asset_type, or status: ')

    for x in range(0, len(list)):
        if row_select in list[x]:
            del list[x]
            list.append(list[x])
            print(list[x])


while True:
    main()
    again = input('Do you want to keep going? y/n: ')
    if again == 'y' or 'yes':
        continue
    else:
        quit()
