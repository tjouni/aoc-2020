def solve(l):
    diff = [l[i + 1] - l[i] for i in range(len(l) - 1)]
    res1 = diff.count(1) * diff.count(3)
    res = {0: 1}
    for x in l[1:]:
        res[x] = res.get(x - 1, 0) + res.get(x - 2, 0) + res.get(x - 3, 0)
    res2 = res[l[-1]]
    return res1, res2


def main():
    l = open("day_10.in").read().splitlines()
    l = sorted([int(s) for s in l])
    l = [0] + l + [l[-1] + 3]
    print(solve(l))


if __name__ == "__main__":
    main()
