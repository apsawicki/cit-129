import re
# lambda

# list1 = [5]
# newlist = 5
#
# for y in range(1, 5):
#     newlist -= 1
#     list1[0] = list1[0] * newlist
#     factorial = list(map(lambda x: x, list1))
#     print(factorial)

# regular expressions

# line = "The Stone Sky, by N.K. Jemisin"
# p = re.compile(', by ')
# m = p.search(line)
# if m:
#     print('Title: ' + line[:m.start()])
#     print('Author: ' + line[m.end():])

# line = "The Stone Sky, by N.K. Jemisin"
# pattern = '([a-zA-Z]+)\s[a-zA-Z]+\s([a-zA-z]+)'
# p = re.compile(pattern)
# m = p.search(line)
# if m:
#     print(m.group(1))

# line = "The Stone Sky, by N.K. Jemisin(Orbit)"
# p = re.compile('([a-zA-Z\s]+)(, by )([a-zA-Z\s]+)')
# m = p.search(line)
# if m:
#     print(m.group(1))
#     print(m.group(3))
#     print(m.group(4))

#
# class myError(Exception):
#     pass
#
# try:
#     raise myError
# except myError:
#     print('-executed or not-?')
