def read_grid(filename):
    # read input file
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    # all possible directions
    directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
    count = 0
    
    # check every position
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if all(0 <= r+i*dx < rows and 0 <= c+i*dy < cols and 
                      grid[r+i*dx][c+i*dy] == "XMAS"[i] for i in range(4)):
                    count += 1
    return count

def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    # check positions that could be center of X pattern
    for r in range(rows-2):
        for c in range(1, cols-1):
            # check if:
            # 1. center is 'A'
            # 2. one diagonal forms 'MAS' or 'SAM'
            # 3. other diagonal forms 'MAS' or 'SAM'
            if (grid[r+1][c] == 'A' and 
                any(x+y == 'MS' for x,y in [(grid[r][c-1], grid[r+2][c+1]), 
                                          (grid[r][c+1], grid[r+2][c-1])]) and
                any(x+y == 'MS' for x,y in [(grid[r][c+1], grid[r+2][c-1]), 
                                          (grid[r][c-1], grid[r+2][c+1])])):
                count += 1
    return count

def main():
    grid = read_grid("input.txt")
    print(f"XMAS appears {count_xmas(grid)} times")
    print(f"X-MAS appears {count_x_mas(grid)} times")

if __name__ == "__main__":
    main()
