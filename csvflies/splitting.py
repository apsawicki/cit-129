name_file = open('names.txt', 'r')
line_reader = name_file.readlines()

for x in line_reader:
    second_name = x.split(" ")[1]
    first_name = x.split(" ")[0]
    print('Good evening Dr. ' + second_name + 'Would you mind if I call you ' + first_name)
