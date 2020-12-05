import re


fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


def first(s):

    passports = s.split("\n\n")
    result = 0
    for passport in passports:
        valid = True
        pairs = passport.split()
        keys = []
        for pair in pairs:
            key, _ = pair.split(":")
            keys.append(key)
        for field in fields:
            if field not in keys and field != "cid":
                valid = False
        if valid:
            result += 1
    print(result)


def second(s):
    def validate_years(items):
        try:
            if (
                int(items["byr"]) >= 1920
                and int(items["byr"]) <= 2002
                and int(items["iyr"]) >= 2010
                and int(items["iyr"]) <= 2020
                and int(items["eyr"]) >= 2020
                and int(items["eyr"]) <= 2030
            ):
                return True
        except:
            return False

    def validate_hgt(items):
        try:
            units = items["hgt"][-2:]
            value = int(items["hgt"][:-2])
            if units == "cm" and value >= 150 and value <= 193:
                return True
            if units == "in" and value >= 59 and value <= 76:
                return True
        except:
            return False

    def validate_hcl(items):
        try:
            if re.match(r"^\#[0-9a-f]{6}$", items["hcl"]):
                return True
        except:
            return False

    def validate_ecl(items):
        if items["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True

    def validate_pid(items):
        if re.match("^[0-9]{9}$", items["pid"]):
            return True

    passports = s.split("\n\n")
    result = 0
    for passport in passports:
        valid = True
        pairs = passport.split()
        items = {}
        for pair in pairs:
            key, value = pair.split(":")
            items[key] = value
        for field in fields:
            if field not in items and field != "cid":
                valid = False
        if (
            valid
            and validate_years(items)
            and validate_hgt(items)
            and validate_hcl(items)
            and validate_ecl(items)
            and validate_pid(items)
        ):
            result += 1
    print(result)


def main():
    s = open("day_4.in").read()
    first(s)
    second(s)


if __name__ == "__main__":
    main()
