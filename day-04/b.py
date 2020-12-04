import re
import uuid

class InvalidPassportFieldError(BaseException):
    pass


class ValidatedField(object):
    def __init__(self, func):
        self.func = func
        self.id = uuid.uuid1()
    
    def __get__(self, obj, objtype):
        return getattr(obj, f"validated-field-{self.id}", None)

    def __set__(self, obj, val):
        try:
            is_valid = self.func(val)
        except:
            is_valid = False

        if is_valid:
            setattr(obj, f"validated-field-{self.id}", val)
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
        pairs = re.findall("((?:byr|iyr|eyr|hgt|hcl|ecl|pid|cid):[a-z0-9#]+)", text)
        for pair in pairs:
            key, val = pair.split(":")
            setattr(passport, key, val)
        return passport
    
    def is_valid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and \
               self.hcl and self.ecl and self.pid
    
    def __repr__(self):
        return f"<Password byr={self.byr} iyr={self.iyr} eyr={self.eyr} hcl={self.hcl} ecl={self.ecl} pid={self.pid} hgt={self.hgt} cid={self.cid}>"


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
