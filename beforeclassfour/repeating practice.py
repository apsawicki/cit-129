main = {}

main['question_name'] = input('What is your name:   ')
main['last_name'] = input('What is your last name:   ')
main['number_nicknames'] = int(input('How many nicknames do you have:   '))

y = int(main['number_nicknames'])

main['nicknames'] = []
for x in range(0, y):
        main['ask_nickname'] = input('What is your nickname:   ')
        main['nicknames'].append(main['ask_nickname'])
        del(main['ask_nickname'])

main['asking_more'] = input('Do you have any more nicknames? yes/no:   ')
if main['asking_more'] == 'no':
    print(main['question_name'])
    print(main['last_name'])
    print(main['nicknames'])

