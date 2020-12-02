import re

class Password:
    @classmethod
    def parse(cls, line):
        s = re.search("(\d+)-(\d+) (\w): (\w+)", line)
        min = int(s.group(1))
        max = int(s.group(2))
        letter = s.group(3)
        pw = s.group(4)
        return cls(min, max, letter, pw)
    
    def __init__(self, min, max, letter, pw):
        self.min = min
        self.max = max
        self.letter = letter
        self.pw = pw
    
    def is_valid(self):
        num = 0
        for c in self.pw:
            if c == self.letter:
                num += 1
        return num >= self.min and num <= self.max

if __name__ == "__main__":
    valid_count = 0
    with open("day-02/input.txt") as lines:
        for line in lines:
            p = Password.parse(line)
            if p.is_valid():
                valid_count += 1
    print(f"Valid password count: {valid_count}")