def first(ins, accumulator=0, i=0, second=False):
    program = ins.copy()
    while True:
        idx = i
        instruction = program[i]
        try:
            operation, argument = instruction.split(" ")
        except:
            if second:
                return False
            else:
                print(accumulator)
                break
        if operation == "acc":
            accumulator += int(argument)
        elif operation == "jmp":
            i += int(argument) - 1
        i += 1
        if i >= len(program):
            break
        program[idx] = "done"
    return accumulator


def second(ins):
    accumulator = 0
    i = 0
    program = ins.copy()
    replacement = {"nop": "jmp", "jmp": "nop"}
    while True:
        instruction = program[i]
        mod = program.copy()
        operation, argument = instruction.split(" ")
        if operation in replacement:
            mod[i] = f"{replacement[operation]} {argument}"
            if result := first(mod, accumulator=accumulator, i=i, second=True):
                print(result)
                break
        if operation == "acc":
            accumulator += int(argument)
        elif operation == "jmp":
            i += int(argument) - 1
        i += 1


def main():
    ins = open("day_8.in").read().splitlines()
    first(ins)
    second(ins)


if __name__ == "__main__":
    main()
