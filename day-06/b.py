sum = 0
with open("day-06/input.txt") as file:
    entries = file.read().split("\n\n")
    for entry in entries:
       responses = entry.split("\n")
       sets = [set(r) for r in responses]
       sum += len(sets[0].intersection(*sets[1:]))
print(f"Sum of counts: {sum}")