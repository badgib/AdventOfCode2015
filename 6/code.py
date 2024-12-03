import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.readlines() 
    
grid_part1 = {}
grid_part2 = {}

def parse_instruction(line):
    match = re.match(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', line)
    if match:
        action, x1, y1, x2, y2 = match.groups()
        return action, int(x1), int(y1), int(x2), int(y2)
    return None

def apply_instruction(action, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            # Part 1 logic
            if action == "turn on":
                grid_part1[(x, y)] = 1
                grid_part2[(x, y)] = grid_part2.get((x, y), 0) + 1
            elif action == "turn off":
                grid_part1[(x, y)] = 0
                grid_part2[(x, y)] = max(0, grid_part2.get((x, y), 0) - 1)
            elif action == "toggle":
                grid_part1[(x, y)] = 1 - grid_part1.get((x, y), 0)
                grid_part2[(x, y)] = grid_part2.get((x, y), 0) + 2

for line in lines:
    instruction = parse_instruction(line)
    if instruction:
        apply_instruction(*instruction)

part1_result = sum(grid_part1.values())
part2_result = sum(grid_part2.values())

print(f"First problem: {part1_result}")
print(f"Second problem: {part2_result}")
