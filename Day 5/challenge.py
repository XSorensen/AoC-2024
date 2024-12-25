import re

def main():
    print("Task 1:")
    task1()

    print("\nTask 2:")
    task2()
    return None

def task1():
    with open("rules.txt", "r") as inFile:
        stream = inFile.read()    
        pattern = "(\\d+)\\|(\\d+)"
        prog = re.compile(pattern)
        rules_matches = prog.findall(stream)

    with open("updates.txt", "r") as inFile:
        stream = inFile.read()
        updates = stream.splitlines()
        int_updates = []
        for update in updates:
            int_updates.append([int(x) for x in update.split(",")])
            
    # dictonary of lists
    # int key corresponds to the list of pages that cannot be printed before it
    rules_dict = {}
    for rule in rules_matches:
        if int(rule[0]) in rules_dict:
            rules_dict[int(rule[0])].append(int(rule[1]))
        else:
            rules_dict[int(rule[0])] = [int(rule[1])]


    sum_of_middle_pages = 0
    for update in int_updates:
        if(valid_update(update, rules_dict)):
            sum_of_middle_pages += update[len(update) // 2]

    print(f"Total: {sum_of_middle_pages}")

    return None

def valid_update(update, rules):
    printed_pages = []

    for page in update:
        print(f"Page: {page}")
        # if the page has special print rules
        if page in rules:
            barred_pages = rules[page]
            # print(f"BarredPages: {barred_pages}")
            for i in barred_pages:
                if i in printed_pages:
                    # print(f"i: {i}")
                    # print(f"Printed pages: {printed_pages}")
                    return False
        
        printed_pages.append(page)    

    return True

def task2():
    return None

if __name__ == "__main__":
    main()


