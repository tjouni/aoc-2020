def first(l):
    for i, number in enumerate(l):
        if i >= 25:
            preamble = l[i - 25 : i]
            valid = False
            for j, a in enumerate(preamble):
                for k, b in enumerate(preamble):
                    if j != k and number == a + b:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                return number


def second(l, x):
    for i, y in enumerate(l):
        j = i + 1
        while y < x:
            y += l[j]
            j += 1
        if y == x:
            return max(l[i : j + 1]) + min(l[i : j + 1])


def main():
    l = open("day_9.in").read().splitlines()
    l = [int(s) for s in l]
    res1 = first(l)
    res2 = second(l, res1)
    print(f"{res1}, {res2}")


if __name__ == "__main__":
    main()
