import re

class Password:
    @classmethod
    def parse(cls, line):
        s = re.search("(\d+)-(\d+) (\w): (\w+)", line)
        index_a = int(s.group(1)) - 1  # index inputs are 1-based
        index_b = int(s.group(2)) - 1  # index inputs are 1-based
        letter = s.group(3)
        pw = s.group(4)
        return cls(index_a, index_b, letter, pw)

    def __init__(self, index_a, index_b, letter, pw):
        self.index_a = index_a
        self.index_b = index_b
        self.letter = letter
        self.pw = pw
    
    def is_valid(self):
        at_a = self.pw[self.index_a] == self.letter
        at_b = self.pw[self.index_b] == self.letter
        return (at_a or at_b) and not (at_a and at_b)

if __name__ == "__main__":
    valid_count = 0
    with open("day-02/input.txt") as lines:
        for line in lines:
            p = Password.parse(line)
            if p.is_valid():
                valid_count += 1
    print(f"Valid password count: {valid_count}")