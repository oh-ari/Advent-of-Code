def find_paths_p1(grid, start):
    # bfs to count reachable 9's
    visited, queue, nines = set(), [(start, 0)], set()
    while queue:
        (r, c), h = queue.pop(0)
        if (r, c) in visited: continue
        visited.add((r, c))
        if grid[r][c] == 9: nines.add((r, c))
        for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and 
                grid[nr][nc] == h + 1):
                queue.append(((nr, nc), h + 1))
    return len(nines)

def find_paths_p2(grid, start):
    # dfs to count all possible paths to 9's
    def dfs(pos, h, path):
        r, c = pos
        if grid[r][c] == 9: return 1  # found a path
        return sum(dfs((nr,nc), h+1, path | {(nr,nc)})  # try all valid neighbors
                  for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
                  if (nr,nc) not in path and 0 <= nr < len(grid) and 
                     0 <= nc < len(grid[0]) and grid[nr][nc] == h + 1)
    return dfs(start, 0, {start})

# load grid from file
grid = [list(map(int, line.strip())) for line in open('input.txt')]
p1 = p2 = 0

# find all trailheads (height 0) and sum their scores
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            p1 += find_paths_p1(grid, (r, c))
            p2 += find_paths_p2(grid, (r, c))

print(f"Part 1: {p1}\nPart 2: {p2}")
