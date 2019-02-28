newFile = open('myfirstfile_sp19.txt', 'a')
numbers = '0123456789'
for x in range(0, len(numbers)):
    something = numbers[0: len(numbers) - x]
    newFile.write(something)
    newFile.write('\n')
