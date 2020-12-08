class InfiniteLooper:
    @classmethod
    def parse(cls, text):
        commands = []
        for line in text.split("\n"):
            cmd, num = line.split(" ")
            commands.append((cmd, int(num), False))
        return cls(commands)
    
    def __init__(self, commands):
        # [(command, number, was_visited)]
        self.commands = commands
    
    def run(self, line_number=0, acc=0):
        cmd, num, visited = self.commands[line_number]
        if visited:
            return acc
        self.commands[line_number] = (cmd, num, True)

        if cmd == 'acc':
            return self.run(line_number + 1, acc + num)
        elif cmd == 'nop':
            return self.run(line_number + 1, acc)
        elif cmd == 'jmp':
            return self.run(line_number + num, acc)
        else:
            raise(Exception(f"Bad command value {cmd}"))
    
if __name__ == '__main__':
    with open("day-08/input.txt") as file:
        il = InfiniteLooper.parse(file.read())
        result = il.run()
        print(f"Accumulated value: {result}")