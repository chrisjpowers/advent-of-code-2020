target_num = 27911108
all_nums = []

with open("day-09/input.txt") as file:
    for line in file:
        all_nums.append(int(line.strip()))

def find_addends(target, nums):
    for j, x in enumerate(nums):
        for k, y in enumerate(nums[j+1:]):
            if x + y == target:
                return (x, y)

for i, first_num in enumerate(all_nums):
    nums = [first_num]
    sum = first_num
    for j, num in enumerate(all_nums[i+1:]):
        sum += num
        nums.append(num)
        if sum == target_num:
            print(f"Nums: {nums}")
            print(f"Weakness: {min(nums) + max(nums)}")
            exit(0)
        if sum > target_num:
            break
