import re

with open("day-07/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

# {color: [(count, child_color)]}
lookup = {}

for line in lines:
    holder_color, rest = line.split(" bags contain ")
    m = re.findall("(\d) ([a-z][a-z ]+) bag", rest)
    lookup[holder_color] = [(int(count), color) for count, color in m]

def recursive_color_count(holder_color):
    sum = 0
    for count, color in lookup.get(holder_color, []):
        sum += (count * recursive_color_count(color)) + count
    return sum

print(f"Color sum: {recursive_color_count('shiny gold')}")