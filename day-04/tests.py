from unittest import TestCase
from b import Passport, InvalidPassportFieldError

class TestDay4(TestCase):
    def assert_parse_valid(self, text):
        p = Passport.parse(text)
        self.assertTrue(p.is_valid())
    
    def assert_parse_invalid(self, text):
        try:
            p = Passport.parse(text)
            if p:
                self.fail()
        except InvalidPassportFieldError:
            self.assertTrue(True)

    def assert_valid(self, key, val):
        p = Passport()
        setattr(p, key, val)
        self.assertTrue(True)
    
    def assert_invalid(self, key, val):
        try:
            p = Passport()
            setattr(p, key, val)
            self.fail()
        except InvalidPassportFieldError:
            self.assertTrue(True)
            
    def test_valid_case(self):
        p = Passport()
        p.byr = 2002
        p.iyr = 2015
        p.eyr = 2025
        p.hgt = "60in"
        p.hcl = "#123abc"
        p.ecl = "brn"
        p.pid = "000000001"
        self.assertTrue(p.is_valid())
    
    def test_byr(self):
        self.assert_valid('byr', '1920')
        self.assert_valid('byr', '1970')
        self.assert_valid('byr', '2002')
        self.assert_invalid('byr', '1919')
        self.assert_invalid('byr', '2003')
        self.assert_invalid('byr', 'foo')
    
    def test_iyr(self):
        self.assert_valid('iyr', '2010')
        self.assert_valid('iyr', '2015')
        self.assert_valid('iyr', '2020')
        self.assert_invalid('iyr', '2009')
        self.assert_invalid('iyr', '2021')
        self.assert_invalid('iyr', 'foo')

    def test_eyr(self):
        self.assert_valid('eyr', '2020')
        self.assert_valid('eyr', '2025')
        self.assert_valid('eyr', '2030')
        self.assert_invalid('eyr', '2019')
        self.assert_invalid('eyr', '2031')
        self.assert_invalid('eyr', 'foo')
    
    def test_hgt(self):
        self.assert_valid('hgt', '150cm')
        self.assert_valid('hgt', '170cm')
        self.assert_valid('hgt', '193cm')
        self.assert_valid('hgt', '59in')
        self.assert_valid('hgt', '68in')
        self.assert_valid('hgt', '76in')
        self.assert_invalid('hgt', '149cm')
        self.assert_invalid('hgt', '194cm')
        self.assert_invalid('hgt', '58in')
        self.assert_invalid('hgt', '77in')
        self.assert_invalid('hgt', '77')
        self.assert_invalid('hgt', 'foo')
    
    def test_hcl(self):
        self.assert_valid('hcl', '#012345')
        self.assert_valid('hcl', '#abcdef')
        self.assert_invalid('hcl', '#abcde')
        self.assert_invalid('hcl', '#abcdeff')
        self.assert_invalid('hcl', '#abcdez')
        self.assert_invalid('hcl', 'abcdef')
        self.assert_invalid('hcl', '000000')

    def test_ecl(self):
        for clr in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            self.assert_valid('ecl', clr)
        self.assert_invalid('ecl', 'foo')
        self.assert_invalid('ecl', '#123456')
    
    def test_pid(self):
        self.assert_valid('pid', '000000001')
        self.assert_valid('pid', '987654321')
        self.assert_invalid('pid', '9876543210')
        self.assert_invalid('pid', '98765432')
        self.assert_invalid('pid', '98765432f')
    
    def test_parsing(self):
        self.assert_parse_valid("byr:2002 iyr:2015 eyr:2025\nhgt:60in hcl:#123abc ecl:brn pid:000000001")
        self.assert_parse_valid("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f")
        self.assert_parse_valid("eyr:2029 ecl:blu cid:129 byr:1989\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm")
        self.assert_parse_valid("hcl:#888785\nhgt:164cm byr:2001 iyr:2015 cid:88\npid:545766238 ecl:hzl\neyr:2022")
        self.assert_parse_valid("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719")

        self.assert_parse_invalid("eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926")
        self.assert_parse_invalid("iyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946")
        self.assert_parse_invalid("hcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277")
        self.assert_parse_invalid("hgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007")
