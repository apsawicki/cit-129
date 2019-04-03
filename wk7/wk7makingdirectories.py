import os
# making a directory using os

# c:\\users\\apsaw\\PycharmProjects or c:/users/apsaw/PycharmProjects

path = input('Choose your directory path: ')

run = 'yes'
while run == 'yes':
    os.chdir(path)
    name = input('What directory would you like to make: ')
    os.makedirs(name)
    run = input('would you like to make another directory? yes/no: ')
    if input('Do you want to change the path? y/n: ') == 'y':
        path = input('Choose your directory path: ')
    else:
        continue
    if input('would you like to delete a directory? yes/no: ') == 'yes':
        del_path = input('give the path of the directory you would like to delete: ')
        os.remove(del_path)
    else:
        continue

