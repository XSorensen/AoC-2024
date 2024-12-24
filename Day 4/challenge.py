


def main():
    print("Task 1:")
    task1()

    return None

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
                xmas_count += count_xmas_from_index(grid, i, j, rows, cols)

    print(f"Total: {xmas_count}")

    return None

def count_xmas_from_index(grid, row, col, row_count, col_count):
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

if __name__ == "__main__":
    main()