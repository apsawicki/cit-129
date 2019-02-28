main = {}

main['question_name'] = input('What is your name:   ')
main['last_name'] = input('What is your last name:   ')
main['number_nicknames'] = input('How many nicknames do you have:   ')

y = int(main['number_nicknames'])

main['nicknames'] = []
for x in range(0,y):
        main['ask_nickname'] = input('What is your nickname:   ')
        main['nicknames'].append(main['ask_nickname'])
        del(main['ask_nickname'])

#for keys,values in main.items():
 #   print()
  #  print(keys)
   # print(values)
print('Your first name is:   ' + main['question_name'])
print('Your last name is:   ' + main['last_name'])
print('Your nickname(s) is/are:   ' + str(main['nicknames']))

# word = "askaliceithinkshe'llknow"
# for x in range(0, len(word), 2):
#    print((word[0 + x: len(word): 2]))
