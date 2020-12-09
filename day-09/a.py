all_nums = []
with open("day-09/input.txt") as file:
    for line in file:
        all_nums.append(int(line.strip()))

def find_addends(target, nums):
    for j, x in enumerate(nums):
        for k, y in enumerate(nums[j+1:]):
            if x + y == target:
                return (x, y)

width = 25
for i, first_num in enumerate(all_nums):
    nums = all_nums[i:i+width]
    target = all_nums[i + width]
    if not find_addends(target, nums):
        print(f"Invalid number: {target}")
        exit(0)
