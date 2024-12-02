import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, "input.txt")

with open(filename) as file:

    lines = file.readlines()

totalarea = 0
totalribbon = 0
for line in lines:
    line = line.split('x')
    line = [int(i) for i in line]
    line.sort()
    area = (2 * line[0] * line[1]) + (2 * line[1] * line[2]) + (2 * line[2] * line[0]) + (line[0] * line[1])
    ribbon = (2 * line[0]) + (2 * line[1]) + (line[0] * line[1] * line[2])
    
    totalarea += area
    totalribbon += ribbon

print(f'First problem: {totalarea}')
print(f'Second problem: {totalribbon}')