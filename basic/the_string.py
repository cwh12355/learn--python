s = 'python-韩文'
print(s)
s1 = s.encode('utf-8')
print(s1)
print(s1.decode('utf-8'))

# tuple type no change
classmates = ('csss','dddd','aaaa')
print('classmates[0] = ',classmates[0])


classmates[0] = 'kbbb'
print(classmates[0])

