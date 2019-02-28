main = {}

y = int(input('How many siblings do you have:   '))

for x in range(0,y):
    sibling_name = input("What is your sibling's name:   ")
    main['sibling_stuff'] = {'Age': input("What is their age:   "), 'birthday': input('When is their birthday:   ')}
    main[str(sibling_name)] = main['sibling_stuff']
    del main['sibling_stuff']
print(main)
