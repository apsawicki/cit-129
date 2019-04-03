peer_info = {}

peer_info['name'] = input('What is your name:   ')
hobby_list = [input('What is one of your hobbies:   ')]
other_hobby = input('Do you have any more hobbies? y/n:   ')


while other_hobby == 'y':
    hobby2 = input('What is another hobby:   ')
    hobby_list.append(hobby2)
    other_hobby = input('Do you have any more hobbies:   ')

os_system = []
os_system['system_name'] = input('What is your favorite operating system:   ')
other_system = input('Do you like any other operating systems:   ')

while other_system == 'y' :
    system2 = input("What is the name of the other system you like:    ")
    os_system['system_name'].append[system2]
    other_system = input('Do you like any other operating systems:   ')


# We have to make a function that asks them what their favorite OS is first, make it the dictionary, then append all of the information onto it.
# We also need to create a function that appends all of our other dictionaries into faveOS.

peer_info['faveOS'] = [os_system]
peer_info['hobby'] = hobby_list
print(peer_info['name'])
print(peer_info['hobby'])

