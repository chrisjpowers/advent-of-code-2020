lookup = {}
with open('day-01/a-input.txt') as file:
    for line in file:
        parsed_int = int(line.strip())
        target = 2020 - parsed_int
        if lookup.get(target):
            print(f"Num: {parsed_int}")
            print(f"Target: {target}")
            print(f"Multiplied: {parsed_int * target}")
            exit(0)
        lookup[parsed_int] = True
print("Oof, no match found")