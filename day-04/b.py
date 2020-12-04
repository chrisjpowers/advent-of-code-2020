import re

class InvalidPassportFieldError(BaseException):
    pass


class ValidatedField:
    def __init__(self, func):
        self.func = func
        self.value = None
    
    def __get__(self, obj, objtype):
        return self.value

    def __set__(self, obj, val):
        try:
            is_valid = self.func(val)
        except:
            is_valid = False

        if is_valid:
            self.value = val
        else:
            raise(InvalidPassportFieldError(f"Invalid value {val}"))


def validate_height(hgt):
    m = re.match("^(\d{2,3})(cm|in)$", hgt)
    if not m:
        return False
    num = int(m[1])
    if m[2] == "cm":
        return num >= 150 and num <= 193
    else:
        return num >= 59 and num <= 76


class Passport:
    byr = ValidatedField(lambda byr: int(byr) >= 1920 and int(byr) <= 2002)
    iyr = ValidatedField(lambda iyr: int(iyr) >= 2010 and int(iyr) <= 2020)
    eyr = ValidatedField(lambda eyr: int(eyr) >= 2020 and int(eyr) <= 2030)
    hgt = ValidatedField(lambda hgt: validate_height(hgt))
    hcl = ValidatedField(lambda hcl: re.match("^#[0-9a-f]{6}$", hcl))
    ecl = ValidatedField(lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    pid = ValidatedField(lambda pid: re.match("^[0-9]{9}$", pid))
    cid = ValidatedField(lambda cid: True)

    @classmethod
    def parse(cls, text):
        passport = cls()
        data = {}
        pairs = re.findall("(\S+:\S+)", text)
        for pair in pairs:
            key, val = pair.split(":")
            if key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']:
                setattr(passport, key, val)
        return passport
    
    def is_valid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and \
               self.hcl and self.ecl and self.pid


if __name__ == '__main__':
    with open("day-04/input.txt") as file:
        entries = file.read().split("\n\n")
    count = 0
    for entry in entries:
        try:
            p = Passport.parse(entry)
            if p.is_valid():
                count += 1
        except InvalidPassportFieldError as e:
            next
    print(f"Valid passport count: {count}")
