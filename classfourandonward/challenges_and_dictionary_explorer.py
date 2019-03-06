# problem 1
# for x in range(0, 101, 2):
#    print(x, end=' ')

# word = 'kaboom'
# x = 3
# print(word[0: x])

# problem 2
# word = 'KABOOM'
# y = 3
# for x in range(0, len(word)):
#    print((word[0 + x:1 + x] + ' ')* y, end='')

# problem 3
# word = "askaliceithinkshe'llknow"
# for x in range(0, len(word), 2):
#     print((word[x: 1 + x: 2] + ' '), end=' ')

# problem 4
# i didn't understand what to do for problem 4

# problem 5
# listoflists = [['mn', 'pa', 'ut'], ['b', 'p', 'c'], ['echo', 'charlie', 'tango']]
# labels = {"state": "US State Abbr: ", "element": "Chemical Element: ", "alpha": "Phonetic Call: "}

# for i in range(0, len(listoflists[1])):
#     if len(listoflists[1]) > 0:
#         print((labels["element"]), str(listoflists[1][i]), end='\n')
# for j in range(0, len(listoflists[0])):
#     if len(listoflists[0]) > 1:
#        print((labels["state"]) * 3, str(listoflists[0][j]), end='\n')
# for k in range(0, len(listoflists[2])):
#     if len(listoflists[2]) > 2:
#        print((labels["alpha"]) * 3, str(listoflists[2][k]), end='\n')

# Dictionary cursor

peer_info = {
    'dict_names': {'alex', 'owen', 'eric'},
    'dict_food': {'chips', 'water', 'orange'},
    'dict_animals': {'dog', 'cat', 'mouse'},
}


def dive_deeper():
    print(peer_info.keys())
    x = input('Select an option: ')
    if x in peer_info.keys():
        print(peer_info[x])


def editor():
    j = input('Would you like to edit? y/n: ')
    if j == 'y':
        y = input('What do you want to edit: ')
        if y not in peer_info:
            new_key = input('What do you want to change it to: ')
            [y].append(new_key)
            del(peer_info[y])
            print(peer_info.keys())
        else:
            print('it didnt work')
            # use while instead of if


dive_deeper()
editor()

# def selection():
#     x = input('What do you select: ')
#     if x in peer_info.keys():
#         print('hello')

# book page 165 peer_info.update
# for x in peer_info:
#     print('dict_names', end='\n')
#     print('dict_food', end='\n')
#     print('dict_animals', end='\n')
#     dive_deeper = input('Do you wish to dive deeper? y/n:  ')
#     if dive_deeper == 'y':
#         sel_val = input('Select a value:  ')
#         if sel_val == '1':
#             print(peer_info['dict_names'])
#             edit_string = input('Do you wish to edit the strings shown? y/n:  ')
#             if edit_string == 'y':
#                 sel_val = input('Select a value:  ')
#                 if sel_val == '1':
#                     change = input('What do you want to change it to:  ')
#                     peer_info.setdefault(change)
#                     print(peer_info['dict_names'])
#         if sel_val == '2':
#             print(peer_info['dict_food'])
#         if sel_val == '3':
#             print(peer_info['dict_animals'])#
