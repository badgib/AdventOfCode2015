import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = [line.strip() for line in file.readlines()]

literal_lengths = sum(len(line) for line in lines)
memory_lengths = sum(len(eval(line)) for line in lines)
part1_result = literal_lengths - memory_lengths

encoded_lengths = sum(len(line.replace('\\', '\\\\').replace('"', '\\"')) + 2 for line in lines)
part2_result = encoded_lengths - literal_lengths

print(f"First problem: {part1_result}")
print(f"Second problem: {part2_result}")
