sum = 0
with open("day-06/input.txt") as file:
    entries = file.read().split("\n\n")
    for entry in entries:
       sum += len(set(entry.replace("\n",''))) 
print(f"Sum of counts: {sum}")