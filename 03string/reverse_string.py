s = input('Enter String:')
print(s[::-1])


rev = ''
for i in s:
    rev = i + rev
print(rev)
