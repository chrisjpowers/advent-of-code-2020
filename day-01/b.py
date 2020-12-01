nums = []
with open('day-01/a-input.txt') as file:
    for line in file:
        parsed_int = int(line.strip())
        nums.append(parsed_int)

nums = sorted(nums)

for i, x in enumerate(nums):
    for j, y in enumerate(nums):
        if j <= i:
            continue
        if x + y >= 2020:
            break
        for k, z in enumerate(nums):
            if k <= j:
                continue
            sum = x + y + z
            if sum > 2020:
                break
            if sum == 2020:
                print(f"x: {x}")
                print(f"y: {y}")
                print(f"z: {z}")
                print(f"Product: {x * y * z}")
                exit(0)
