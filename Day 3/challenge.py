import re

def main():
    print("Task 1:")
    task1()

    print("\nTask 2:")
    task2()

    return None

def task1():
    pattern = "mul\\((\\d{1,3}),(\\d{1,3})\\)"
    prog = re.compile(pattern)

    with open("input.txt", "r") as inFile:
        stream = inFile.read()
        result = prog.findall(stream)

    total = 0
    for pair in result:
        total += int(pair[0]) * int(pair[1])

    print(f"Total: {total}")
    return None

def task2():
    pattern = "mul\\((\\d{1,3}),(\\d{1,3})\\)|(do\(\))|(don't\(\))"
    prog = re.compile(pattern)

    with open("input.txt", "r") as inFile:
        stream = inFile.read()
        result = prog.findall(stream)

    total = 0
    enabled = True

    # match structure is (first num, second num, do command, don't command)
    # the numbers are empty if it is a command
    # the commands are empty if it is a mul instruction
    for match in result:
        if(match[2] == "do()"):
            enabled = True
        elif (match[3] == "don't()"):
            enabled = False
        elif enabled:
            total += int(match[0]) * int(match[1])

    print(f"Total: {total}")
    return None

if __name__ == "__main__":
    main()