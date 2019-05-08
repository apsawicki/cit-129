# problem 1
# for x in range(0, 101, 2):
#    print(x, end=' ')
#
# problem 2
# word = 'KABOOM'
# for x in range(0, len(word)):
#     print((word[x:x + 1] + ' ') * 3, end='')
#
# problem 3
# word = "askaliceithinkshe'llknow"
# for x in range(0, len(word), 2):
#     print((word[x: 1 + x: 2] + ' '), end=' ')
#
# problem 4
# i didn't understand what to do for problem 4
#
# problem 5
# listoflists = [['mn', 'pa', 'ut'], ['b', 'p', 'c'], ['echo', 'charlie', 'tango']]
# labels = {"state": "US State Abbr: ", "element": "Chemical Element: ", "alpha": "Phonetic Call: "}
#
# for i in range(0, len(listoflists[1])):
#     if len(listoflists[1]) > 0:
#         print((labels["element"]), str(listoflists[1][i]), end='\n')
# for j in range(0, len(listoflists[0])):
#     if len(listoflists[0]) > 1:
#        print((labels["state"]) * 3, str(listoflists[0][j]), end='\n')
# for k in range(0, len(listoflists[2])):
#     if len(listoflists[2]) > 2:
#        print((labels["alpha"]) * 3, str(listoflists[2][k]), end='\n')
#
# Dictionary cursor

peer_info = {
    'dict_names': ['alex', 'owen', 'eric'],
    'dict_food': ['chips', 'water', 'orange'],
    'dict_animals': ['dog', 'cat', 'mouse']
}

option = ''


def dive_deeper():
    print(peer_info.keys())
    global option
    option = input('Select an option: ')
    if option in peer_info.keys():
        print(peer_info[option])


def editor():
    query = input('Would you like to edit? y/n: ')
    if query == 'y':
        edit = int(input('Which number item do you want to change: '))
        new_key = input('What do you want to change it to: ')
        peer_info[option].append(new_key)
        del(peer_info[option][edit])
        print(peer_info[option])


while True:
    dive_deeper()
    editor()
    again = input('Wanna keep going? y/n: ')
    if again == 'y' or 'yes':
        continue
    else:
        quit()

