import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, "input.txt")

with open(filename) as file:

    line = file.readline()

position = [0, 0]
presentpos = []
for i in range(len(line)):
    presentpos.append((position[0], position[1]))
    if line[i] == ">":
        position[0] += 1
    elif line[i] == "<":
        position[0] -= 1
    elif line[i] == "^":
        position[1] += 1
    elif line[i] == "v":
        position[1] -= 1

duplicates = {}
for presepos in presentpos:
    duplicates[presepos] = duplicates.get(presepos, 0) + 1

print(f'First problem: {len(duplicates)}')

santapos = [0, 0]
robopos = [0, 0]
santaspres = []

for i in range(0, len(line), 2):
    santaspres.append((santapos[0], santapos[1]))
    santaspres.append((robopos[0], robopos[1]))
    if line[i] == ">":
        santapos[0] += 1
    elif line[i] == "<":
        santapos[0] -= 1
    elif line[i] == "^":
        santapos[1] += 1
    elif line[i] == "v":
        santapos[1] -= 1

    if line[i + 1] == ">":
        robopos[0] += 1
    elif line[i + 1] == "<":
        robopos[0] -= 1
    elif line[i + 1] == "^":
        robopos[1] += 1
    elif line[i + 1] == "v":
        robopos[1] -= 1

santadupes = {}
for anypres in santaspres:
    santadupes[anypres] = santadupes.get(anypres, 0) + 1

print(f'Second problem: {len(santadupes)}')
