def solve(s):
    boarding_passes = s.split("\n")
    ids = sorted(
        [
            (
                int(
                    seat.replace("F", "0")
                    .replace("B", "1")
                    .replace("L", "0")
                    .replace("R", "1"),
                    2,
                )
            )
            for seat in boarding_passes
        ]
    )
    print(ids[-1])
    for id in range(ids[0], ids[-1]):
        if id not in ids and id - 1 in ids and id + 1 in ids:
            print(id)


def main():
    s = open("day_5.in").read()
    solve(s)


if __name__ == "__main__":
    main()
