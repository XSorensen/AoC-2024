import re

def main():
    print("Task 1:")
    task1()
    print()

    print("Task 2:")
    task2()
    print()

    return

def task1():
    pattern = "(\\d+)   (\\d+)"

    with open("Input.txt", "r") as infile:
        data = infile.read()

        parsed_data = re.findall(pattern, data)
        # print(data)

        l1 = [x[0] for x in parsed_data]
        l2 = [x[1] for x in parsed_data]

        l1.sort()
        l2.sort()

        distance = 0
        for i in range(len(l1)):
            distance += abs(int(l1[i]) - int(l2[i]))
        
        print(f'Distance: {distance}')

    return

def task2():
    pattern = "(\\d+)   (\\d+)"

    with open("Input.txt", "r") as infile:
        data = infile.read()

        parsed_data = re.findall(pattern, data)

        l1 = [x[0] for x in parsed_data]
        l2 = [x[1] for x in parsed_data]

        l1_frequencies = dict()
        l2_frequencies = dict()

        for i in l2:
            if i in l2_frequencies:
                l2_frequencies[i] += 1
            else:
                l2_frequencies[i] = 1

        for i in l1:
            if i in l2_frequencies:
                l1_frequencies[i] = l2_frequencies[i]
            else:
                l1_frequencies[i] = 0

        distance = 0
        for i in l1_frequencies:
            distance += int(i) * l1_frequencies[i]
        
        print(f'Distance: {distance}')

    return

if __name__ == "__main__":
    main()