

def main():
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
            if(valid_level(level)):
                valid_lines += 1

        print(f"Valid Lines: {valid_lines}")
    return

def valid_level(stream):
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

if __name__ == "__main__":
    main()