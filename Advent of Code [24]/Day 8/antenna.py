def input(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def antennas(grid):
    # freq -> coords
    antennas = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                antennas.setdefault(grid[y][x], []).append((x, y))
    return antennas

def collinear(p1, p2, p3):
    # check if points make line
    return (p2[1]-p1[1])*(p3[0]-p2[0]) == (p3[1]-p2[1])*(p2[0]-p1[0])

def antinodes_part1(grid, antennas):
    antinodes = set()
    seen = set()
    
    # handle overlaps
    for positions in antennas.values():
        for pos in positions:
            if pos in seen: antinodes.add(pos)
            seen.add(pos)
    
    # find 2x distance points
    for positions in antennas.values():
        for i, (x1, y1) in enumerate(positions):
            for x2, y2 in positions[i+1:]:
                dx, dy = x2-x1, y2-y1
                for x, y in [(x2-2*dx, y2-2*dy), (x1+2*dx, y1+2*dy)]:
                    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                        antinodes.add((int(x), int(y)))
    return len(antinodes)

def antinodes_part2(grid, antennas):
    antinodes = set()
    
    # find all collinear points
    for positions in antennas.values():
        if len(positions) < 2: continue
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                for i, p1 in enumerate(positions):
                    if any(collinear(p1, p2, (x,y)) 
                          for p2 in positions[i+1:]):
                        antinodes.add((x,y))
                        break
    return len(antinodes)

def solve(filename):
    grid = input(filename)
    antennas = antennas(grid)
    return antinodes_part1(grid, antennas), antinodes_part2(grid, antennas)

if __name__ == "__main__":
    p1, p2 = solve("input.txt")
    print(f"part 1: {p1}\npart 2: {p2}")
