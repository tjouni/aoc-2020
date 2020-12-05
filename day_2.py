def solve(l):
    valid1 = 0
    valid2 = 0
    for s in l:
        rule, password = s.split(": ")
        times, letter = rule.split(" ")
        min, max = times.split("-")
        times = 0
        if password.count(letter) <= int(max) and password.count(letter) >= int(min):
            valid1 += 1
        if letter == password[int(max) - 1]:
            times += 1
        if letter == password[int(min) - 1]:
            times += 1
        if times == 1:
            valid2 += 1
    print(valid1)
    print(valid2)


def main():
    l = open("day_2.in").read().splitlines()
    solve(l)


if __name__ == "__main__":
    main()
