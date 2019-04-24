numbers = []

print('Please choose at least 2 numbers', end='\n')


def inputer():
    num = int(input('Choose a number: '))
    numbers.append(num)
    global stopper
    stopper = input('Do you wish to stop? y/n: ')


def adder():
    print(sum(numbers))


def multiplier():
    for x in range(1, len(numbers)):
        numbers[0] = numbers[x] * numbers[x]
        print(numbers[0])


def decision():
    choice = input('Choose multiply or add: ')
    if choice == 'multiply':
        multiplier()
    if choice == 'add':
        adder()


inputer()

while stopper is 'n':
    inputer()
else:
    decision()

'''
Extension Exercises: 
1. Add subtracting function to the calculator
2. Add standard deviation function without use of the built in stdev function
3. Remove all 'def' functions and rewrite code to use lambda
'''
