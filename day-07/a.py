import re

with open("day-07/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

# {color: [colors it can be in]}
lookup = {}

for line in lines:
    holder_color, rest = line.split(" bags contain ")
    m = re.findall("([a-z][a-z ]+) bag", rest)
    for color in m:
        if color == "no other": next
        lookup[color] = lookup.get(color, [])
        lookup[color].append(holder_color)

def recursive_color_search(color):
    colors = set(lookup.get(color, []))
    for c in colors:
        colors = colors.union(recursive_color_search(c))
    return colors

print(f"Colors: {recursive_color_search('shiny gold')}")
print(f"Color sum: {len(recursive_color_search('shiny gold'))}")