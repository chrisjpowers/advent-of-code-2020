def step(current_jolt, remaining_jolts, one_steps=0, three_steps=0):
    if len(remaining_jolts) == 0:
        return (one_steps, three_steps)
    next_jolt = remaining_jolts[0]
    if next_jolt == current_jolt + 1:
        return step(next_jolt, remaining_jolts[1:], one_steps + 1, three_steps)
    if next_jolt == current_jolt + 2:
        return step(next_jolt, remaining_jolts[1:], one_steps, three_steps)
    if next_jolt == current_jolt + 3:
        return step(next_jolt, remaining_jolts[1:], one_steps, three_steps + 1)
    else:
        print(f"FAIL: {current_jolt}, {next_jolt}")
        exit()

if __name__ == '__main__':
    with open("day-10/input.txt") as file:
        nums = sorted([int(line.strip()) for line in file])
        # Start with a three representing the device
        one_steps, three_steps = step(0, nums, 0, 1)
        print(f"One steps: {one_steps}")
        print(f"Three steps: {three_steps}")
        print(f"Multiplied: {one_steps * three_steps}")
