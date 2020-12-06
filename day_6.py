def solve(s):
    groups = s.split("\n\n")
    result1 = 0
    result2 = 0
    for group in groups:
        answer_counts = {}
        for line in group.split("\n"):
            for c in line.rstrip():
                answer_counts[c] = answer_counts.get(c, 0) + 1
            for _, v in answer_counts.items():
                if v == len(group.split("\n")):
                    result2 += 1
        result1 += len(set(group))
    print(result1)
    print(result2)


def main():
    s = open("day_6.in").read()
    solve(s)


if __name__ == "__main__":
    main()
