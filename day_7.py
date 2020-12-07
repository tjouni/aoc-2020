def search(bags, color, result=[]):
    count = 0
    result.append(color)
    for bag, colors in bags.items():
        if color in colors.keys() and bag not in result:
            count += 1 + search(bags, bag, result)
    return count


def count_bags(bags, color):
    count = 0
    colors = bags.get(color, {})
    for color, n in colors.items():
        count += n + n * count_bags(bags, color)
    return count


def solve(l):
    result1 = 0
    result2 = 0
    bags = {}
    for rule in l:
        bag, contents = rule.split(" bags contain ")
        if contents != "no other bags.":
            if bag not in bags:
                bags[bag] = {}
            for content in contents.split(", "):
                bag_color = " ".join(content.split()[1:-1])
                number_of_bags = content.split()[0]
                if bag_color not in bags[bag]:
                    bags[bag][bag_color] = int(number_of_bags)
    result1 = search(bags, "shiny gold")
    result2 = count_bags(bags, "shiny gold")
    print(result1)
    print(result2)


def main():
    l = open("day_7.in").read().rstrip().splitlines()
    solve(l)


if __name__ == "__main__":
    main()
