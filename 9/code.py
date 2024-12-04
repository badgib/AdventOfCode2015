import os
from itertools import permutations

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = [line.strip() for line in file.readlines()]

distances = {}
cities = set()

for line in lines:
    parts = line.split(" = ")
    distance = int(parts[1])
    city1, city2 = parts[0].split(" to ")
    distances[(city1, city2)] = distance
    distances[(city2, city1)] = distance
    cities.add(city1)
    cities.add(city2)

def calculate_route_distance(route):
    return sum(distances[(route[i], route[i+1])] for i in range(len(route) - 1))

all_routes = permutations(cities)

shortest = float('inf')
longest = float('-inf')

for route in all_routes:
    total_distance = calculate_route_distance(route)
    shortest = min(shortest, total_distance)
    longest = max(longest, total_distance)

print(f"First problem: {shortest}")
print(f"Second problem: {longest}")
