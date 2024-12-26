def main():
    tests()
    print("Task 1:")
    task(valid_level_task1)
    
    print("\nTask 2:")
    task(valid_level_task2_driver)
    return

def task(test_fun):
    with open("input.txt", "r") as infile:
        data = infile.read()
        str_levels = []
        int_levels = []
        lines = data.splitlines()
        
        valid_lines = 0
        
        for line in lines:
            str_levels.append(line.split(" "))

        for level in str_levels:
            curr_arr = []
            for num in level:
                curr_arr.append(int(num))
            int_levels.append(curr_arr)

        for level in int_levels:
            res = test_fun(level)
            # print(res) #FIXME Remove after debugging
            if(res):
                valid_lines += 1

        print(f"Valid Lines: {valid_lines}")
    return

def valid_level_task1(stream):
    if(len(stream) == 1):
        return True 
    
    comparator = None
    if(stream[0] < stream[1]):
        comparator = lambda x, y : x < y
    else:
        comparator = lambda x, y : x > y

    for i in range(len(stream) - 1):
        if(comparator(stream[i], stream[i + 1])):
            if(abs(stream[i] - stream[i + 1]) > 3):
                return False
        else:
            return False
    
    return True

def valid_level_task2_driver(stream):
    if(len(stream) == 1):
        return True 
    
    comparator = None
    if(stream[0] < stream[1]):
        comparator = lambda x, y : x < y
    else:
        comparator = lambda x, y : x > y

    whole_comparator = lambda x, y : (comparator(x, y) and (abs(x - y) <= 3))

    return valid_level_task2_recursive(stream, whole_comparator, False)

def valid_level_task2_recursive(stream, comparator, level_removed):
    if(stream == None):
        return False
    
    level_count = len(stream)
    i = -1
    # while(i < level_count - 2):
    for i in range(level_count - 1):
        # i += 1

        # pairing is valid, move onto next
        if(comparator(stream[i], stream[i + 1])):
            continue

        # exit if a level has already been removed
        if(level_removed):
            return False
        
        # create new arrays without the two potential levels
        curr_removed = dupe_array_without_index(stream, i)
        next_removed = dupe_array_without_index(stream, i + 1)
        
        res = valid_level_task2_recursive(curr_removed, comparator, True) or valid_level_task2_recursive(next_removed, comparator, True)

        # first element has issue, so comparator may need to be changed
        if(i == 1):
            if(stream[1] < stream[2]):
                new_comp = lambda x, y: (x < y and (abs(x - y) <= 3))
            else:
                new_comp = lambda x, y: (x > y and (abs(x - y) <= 3))
            print("Removed first element")
            first_removed = stream[1:]
            res = res or valid_level_task2_recursive(first_removed, new_comp, True)
                
        # returns true if either removing the current level or the next level works
        print(f"Level removed:")
        print(f"Stream: {stream}")
        print(f"Success after removal: {res}")
        print()
        return res
        return valid_level_task2_recursive(curr_removed, comparator, True) or valid_level_task2_recursive(next_removed, comparator, True)

    return True
    
def valid_level_task2(stream):
    print(stream, end=": ")
    removed_level = False
    removed_index = -1
    
    if(len(stream) == 1):
        return True 
    
    comparator = None
    if(stream[0] < stream[1]):
        comparator = lambda x, y : x < y
    else:
        comparator = lambda x, y : x > y

    whole_comparator = lambda x, y : (comparator(x, y) and (abs(x - y) <= 3))

    level_count = len(stream)
    i = -1
    while(i < level_count - 2):
        i += 1
        
        # perfect match
        if(whole_comparator(stream[i], stream[i + 1])):
            continue
        
        # level is wrong if a level has already been removed
        # and a new one is malformed
        if(removed_level):
            return False

        if(0 < i and i < level_count - 3):
            valid_if_remove_i = whole_comparator(stream[get_preceeding_index(i, removed_index)], stream[i + 1])
            valid_if_remove_i_plus_1 = whole_comparator(stream[i], stream[i + 2])

            if(not (valid_if_remove_i or valid_if_remove_i_plus_1)):
                return False
            




        # first element does not have a preceeding term
        if(i > 0):
            if(whole_comparator(stream[get_preceeding_index(i, removed_index)], stream[i + 1])):
                removed_level = True
                removed_index = i
                continue

        if(i < level_count - 3):
            removed_level = True
            removed_index = i + 1
            if(whole_comparator(stream[i], stream[i + 2])):
                i += 1
            else:
                return False

        if(i == level_count - 3):
            return whole_comparator(stream[i], stream[i + 2])

    return True

def get_preceeding_index(curr_index, removed_index):
    if(removed_index == -1):
        return curr_index - 1
    elif(removed_index == curr_index - 1):
        return curr_index - 2
    else:
        return curr_index - 1

def dupe_array_without_index(arr, index):
    arr_len = len(arr)

    if(index < 0 or index >= arr_len):
        raise IndexError(f"Index {index} out of range of array of length {arr_len}")
    
    ret_arr = [None] * (arr_len - 1)

    assert(len(ret_arr) == len(arr) - 1)

    for i in range(0, index):
        ret_arr[i] = arr[i]
    
    for i in range(index + 1, arr_len):
        ret_arr[i - 1] = arr[i]

    return ret_arr

def tests():
    temp_arr = [0, 1, 2, 3, 4, 5]

    assert(dupe_array_without_index(temp_arr, 2) == [0, 1, 3, 4, 5])

if __name__ == "__main__":
    main()