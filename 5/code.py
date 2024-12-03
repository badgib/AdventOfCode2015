import os
import re


here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "input.txt")

with open(filename) as file:
    lines = file.readlines()

nicelines = 0


for line in lines:
    line = line.strip()

    vowels = 0
    has_double = False
    has_forbidden = False

    for i in range(len(line)):

        if line[i] in "aeiou":
            vowels += 1

        if i < len(line) - 1:
            pair = line[i:i+2]
            if pair in {"ab", "cd", "pq", "xy"}:
                has_forbidden = True
                break

        if i < len(line) - 1 and line[i] == line[i + 1]:
            has_double = True

    if vowels >= 3 and has_double and not has_forbidden:
        nicelines += 1

print(f"First problem: {nicelines}")

def is_contain_pair(string):
    return bool(re.search(r'([a-z][a-z]).*\1', string))

def is_contain_repeat_letter(string):
    return bool(re.search(r'([a-z])[a-z]\1', string))

def is_nice_string(string):
    return is_contain_pair(string) and is_contain_repeat_letter(string)

result = sum(1 for line in lines if is_nice_string(line))

print(f'second problem: {result}')