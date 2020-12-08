from a import InfiniteLooper
from copy import deepcopy

if __name__ == '__main__':
    master_list = []
    with open("day-08/input.txt") as file:
        for line in file:
            cmd, num = line.strip().split(" ")
            master_list.append((cmd, int(num), False))
    
    # Brute force, it's good for the body.
    for i, entry in enumerate(master_list):
        cmd, num, visited = entry
        if cmd == 'acc': next
        new_list = deepcopy(master_list)
        new_cmd = 'jmp' if cmd == 'nop' else 'nop'
        new_list[i] = (new_cmd, num, visited)
        il = InfiniteLooper(new_list)
        result = il.run()
        if il.is_complete:
            print(f"Fixed accumulator: {result}")
            exit(0)
