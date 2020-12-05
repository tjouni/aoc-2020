import numpy as np


def first(s):
    lines = s.split("\n")
    trees = 0
    for i, line in enumerate(lines):
        if line[i * 3 % len(line)] == "#":
            trees += 1
    print(trees)


def second(s):
    lines = s.split("\n")
    trees = [0, 0, 0, 0, 0]
    length = len(lines[0])
    for i, line in enumerate(lines):
        for k, multiplier in enumerate([1, 3, 5, 7]):
            j = i * multiplier % length
            if line[j] == "#":
                trees[k] += 1
        if not i % 2:
            j = i // 2 % length
            if line[j] == "#":
                trees[4] += 1
    print(np.prod(trees))


def main():
    s = open("day_3.in").read()
    first(s)
    second(s)


if __name__ == "__main__":
    main()
