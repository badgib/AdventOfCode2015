import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.readlines() 
    
instructions = {}
for line in lines:
    match = re.match(r"(.*) -> ([a-z]+)", line)
    if match:
        operation, output = match.groups()
        instructions[output] = operation

cache = {}

def evaluate(wire):
    if wire.isdigit():
        return int(wire)

    if wire in cache:
        return cache[wire]

    operation = instructions[wire]

    if "AND" in operation:
        a, b = operation.split(" AND ")
        result = evaluate(a) & evaluate(b)
    elif "OR" in operation:
        a, b = operation.split(" OR ")
        result = evaluate(a) | evaluate(b)
    elif "LSHIFT" in operation:
        a, b = operation.split(" LSHIFT ")
        result = evaluate(a) << int(b)
    elif "RSHIFT" in operation:
        a, b = operation.split(" RSHIFT ")
        result = evaluate(a) >> int(b)
    elif "NOT" in operation:
        a = operation.split("NOT ")[1]
        result = ~evaluate(a) & 0xFFFF
    else:
        result = evaluate(operation)

    cache[wire] = result
    return result

part1_result = evaluate("a")
print(f"First problem: {part1_result}")

cache.clear()
instructions["b"] = str(part1_result)
part2_result = evaluate("a")
print(f"Second problem: {part2_result}")
