import re

class Passport:
    @classmethod
    def parse(cls, text):
        data = {}
        pairs = re.findall("(\S+:\S)", text)
        for pair in pairs:
            key, val = pair.split(":")
            data[key] = val
        return cls(data)
    
    def __init__(self, data):
        self.data = data
    
    def is_valid(self):
        d = self.data
        return d.get('byr') and d.get('iyr') and d.get('eyr') and \
               d.get('hgt') and d.get('hcl') and d.get('ecl') and \
               d.get('pid')

if __name__ == '__main__':
    with open("day-04/input.txt") as file:
        entries = file.read().split("\n\n")
    count = 0
    for entry in entries:
        p = Passport.parse(entry)
        if p.is_valid():
            count += 1
    print(f"Valid passport count: {count}")
