def main():
    print("Task 1:")
    task1()

    print("\nTask 2:")
    task2()

    return None

# find all occurences of XMAS in the puzzle (left, right, diagonal, backwards)
def task1():
    with open("input.txt", "r") as inFile:
        stream = inFile.read()

    lines = stream.splitlines()    
    grid = []

    rows = len(lines)
    cols = len(lines[0])

    for line in lines:
        grid.append(list(line))

    xmas_count = 0
    for i in range(rows):
        for j in range(cols):
            if(lines[i][j] == "X"):
                xmas_count += count_xmas_from_index_task1(grid, i, j, rows, cols)

    print(f"Total: {xmas_count}")

    return None

def task2():
    with open("input.txt", "r") as inFile:
        stream = inFile.read()

    lines = stream.splitlines()    
    grid = []

    rows = len(lines)
    cols = len(lines[0])

    for line in lines:
        grid.append(list(line))

    xmas_count = 0
    for i in range(rows):
        for j in range(cols):
            if(lines[i][j] == "A"):
                if(is_valid_xmas_from_index_task2(grid, i, j, rows, cols)):
                    xmas_count += 1

    print(f"Total: {xmas_count}")

    return None

def count_xmas_from_index_task1(grid, row, col, row_count, col_count):
    match = ["M", "A", "S"]
    toCheck = []
    # xmas length = 4
    # there must be at least 3 open positions between x and the nearest barrier
    
    # vertical bottom up XMAS
    if(row >= 3):
        toCheck.append([grid[row - 1][col], grid[row - 2][col], grid[row - 3][col]])

    # vertical top down XMAS
    if(row <= row_count - 4):
        toCheck.append([grid[row + 1][col], grid[row + 2][col], grid[row + 3][col]])

    # left to right XMAS
    if(col <= col_count - 4):
        # horrizontal
        toCheck.append([grid[row][col + 1], grid[row][col + 2], grid[row][col + 3]])

        # up diagonal
        if(row >= 3):
            toCheck.append([grid[row - 1][col + 1], grid[row - 2][col + 2], grid[row - 3][col + 3]])
            
        # down diagonal
        if(row <= row_count - 4):
            toCheck.append([grid[row + 1][col + 1], grid[row + 2][col + 2], grid[row + 3][col + 3]])

    # right to left XMAS
    if(col >= 3):
         # horrizontal
        toCheck.append([grid[row][col - 1], grid[row][col - 2], grid[row][col - 3]])

        # up diagonal
        if(row >= 3):
            toCheck.append([grid[row - 1][col - 1], grid[row - 2][col - 2], grid[row - 3][col - 3]])
            
        # down diagonal
        if(row <= row_count - 4):
            toCheck.append([grid[row + 1][col - 1], grid[row + 2][col - 2], grid[row + 3][col - 3]])

    count = 0
    # counting the matching checks
    for check in toCheck:
        if(check == match):
            count += 1

    return count

def is_valid_xmas_from_index_task2(grid, row, col, row_count, col_count):
    # early exit if potential xmas does not have enough room
    if(row < 1 or row > row_count - 2):
        return False
    elif(col < 1 or col > col_count - 2):
        return False

    valid_cross = True

    # top left to bottom right diagonal
    if((grid[row - 1][col - 1] == "M" and grid[row + 1][col + 1] == "S")):
        valid_cross = True
    elif((grid[row - 1][col - 1] == "S" and grid[row + 1][col + 1] == "M")):
        valid_cross = True
    else:
        valid_cross = False
    
    # bottom left to bottom right diagonal
    if((grid[row + 1][col - 1] == "M" and grid[row - 1][col + 1] == "S")):
        valid_cross = valid_cross
    elif((grid[row + 1][col - 1] == "S" and grid[row - 1][col + 1] == "M")):
        valid_cross = valid_cross
    else:
        valid_cross = False
    
    return valid_cross

if __name__ == "__main__":
    main()