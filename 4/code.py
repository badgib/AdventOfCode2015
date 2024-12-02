import hashlib

input = 'abcdef'

calhash = ''
i = 0
while calhash[:5] != '00000':

    calhash = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
    i += 1

print(f'First problem: {i - 1}')

sixhash = ''
j = 0
while sixhash[:6] != '000000':

    sixhash = hashlib.md5((input + str(j)).encode('utf-8')).hexdigest()
    j += 1

print(f'Second problem: {j - 1}')