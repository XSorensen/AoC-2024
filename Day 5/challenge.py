import re

def main():
    print("Task 1:")
    task1()

    print("\nTask 2:")
    task2()
    return None

def task1():
    rules, updates = extractData()

    sum_of_middle_pages = 0
    for update in updates:
        if(valid_update(update, rules)):
            sum_of_middle_pages += update[len(update) // 2]

    print(f"Total: {sum_of_middle_pages}")

    return None

def task2():
    return None

def extractData():
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
    
    return [rules_dict, int_updates]

def valid_update(update, rules):
    printed_pages = []

    for page in update:
        # if the page has special print rules
        if page in rules:
            barred_pages = rules[page]
            for i in barred_pages:
                if i in printed_pages:
                    return False
        
        printed_pages.append(page)    

    return True

if __name__ == "__main__":
    main()


