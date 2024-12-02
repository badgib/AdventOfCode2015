import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, "input.txt")

with open(filename) as file:

    line = file.readline()

floor = 0
b_first_basement = False
for i in range(len(line)):
    if line[i] == "(":
        floor += 1
    elif line[i] == ")":
        floor -= 1

    if floor == -1 and b_first_basement == False:
        b_first_basement = True
        print(f'Second problemm: {i + 1}')
    
print(f'First problemm: {floor}')

