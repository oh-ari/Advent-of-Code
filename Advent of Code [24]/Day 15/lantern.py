def read_input(filename):
    # get map and moves from file
    warehouse, moves = [], []
    with open(filename) as f:
        read_map = True
        for line in f:
            if not line.strip(): read_map = False; continue
            if read_map: warehouse.append(list(line.strip()))
            else: moves.extend(list(line.strip()))
    return warehouse, moves

def find_robot(warehouse):
    # find robot pos in grid
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == "@":
                return y, x

def check_available_spot(warehouse, pos_y, pos_x, direction):
    # check if box can move in direction and move it if possible
    if direction == "^":
        for y in range(pos_y - 1, -1, -1):
            if warehouse[y][pos_x] == "#":
                return False
            if warehouse[y][pos_x] == ".":
                warehouse[pos_y][pos_x] = "."
                warehouse[y][pos_x] = "O"
                return True
    elif direction == ">":
        for x in range(pos_x + 1, len(warehouse[0])):
            if warehouse[pos_y][x] == "#":
                return False
            if warehouse[pos_y][x] == ".":
                warehouse[pos_y][pos_x] = "."
                warehouse[pos_y][x] = "O"
                return True
    elif direction == "v":
        for y in range(pos_y + 1, len(warehouse)):
            if warehouse[y][pos_x] == "#":
                return False
            if warehouse[y][pos_x] == ".":
                warehouse[pos_y][pos_x] = "."
                warehouse[y][pos_x] = "O"
                return True
    elif direction == "<":
        for x in range(pos_x - 1, -1, -1):
            if warehouse[pos_y][x] == "#":
                return False
            if warehouse[pos_y][x] == ".":
                warehouse[pos_y][pos_x] = "."
                warehouse[pos_y][x] = "O"
                return True
    return False

def scale_warehouse(warehouse):
    # double width of warehouse for part 2
    maps = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    return [list("".join(maps[c] for c in line)) for line in warehouse]

def get_blocks_to_move(warehouse, x, y, direction):
    # get all connected boxes that need to move
    dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    dy, dx = dirs[direction]
    ny, nx = y + dy, x + dx
    
    if warehouse[ny][nx] == "#": return False, []
    if warehouse[ny][nx] == ".": return True, []
    
    if direction in "<>":
        blocks = [(y, nx if dx > 0 else nx-1)]
        can_move, next_blocks = get_blocks_to_move(warehouse, x + dx*2, y, direction)
        return can_move, blocks + next_blocks
    
    y += dy
    x -= warehouse[ny][nx] == "]"
    blocks = [(y, x)]
    can_move1, blocks1 = get_blocks_to_move(warehouse, x, y, direction)
    if not can_move1: return False, []
    can_move2, blocks2 = get_blocks_to_move(warehouse, x+1, y, direction)
    return can_move1 and can_move2, blocks + blocks1 + blocks2

def simulate_robot(warehouse, moves, part2=False):
    # move robot and boxes around warehouse
    dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    pos_y, pos_x = find_robot(warehouse)
    warehouse[pos_y][pos_x] = "."
    
    if not part2:
        for move in moves:
            dy, dx = dirs[move]
            ny, nx = pos_y + dy, pos_x + dx
            
            if warehouse[ny][nx] == ".":
                pos_y, pos_x = ny, nx
            elif warehouse[ny][nx] == "#":
                continue
            elif check_available_spot(warehouse, ny, nx, move):
                pos_y, pos_x = ny, nx
    else:
        warehouse[pos_y][pos_x + 1] = "."
        for move in moves:
            can_move, blocks = get_blocks_to_move(warehouse, pos_x, pos_y, move)
            if not can_move: continue
            dy, dx = dirs[move]
            for by, bx in blocks:
                warehouse[by][bx:bx+2] = ".."
            for by, bx in blocks:
                warehouse[by+dy][bx+dx:bx+dx+2] = "[]"
            warehouse[pos_y][pos_x] = "."
            pos_y, pos_x = pos_y + dy, pos_x + dx
            warehouse[pos_y][pos_x] = "@"

def calculate_gps_sum(warehouse, part2=False):
    # sum up gps coords of boxes
    target = "[" if part2 else "O"
    return sum(100 * y + x for y in range(len(warehouse)) 
              for x in range(len(warehouse[0])) if warehouse[y][x] == target)

def solve(part):
    # solve part 1 or 2
    warehouse, moves = read_input("input.txt")
    if part == 2: warehouse = scale_warehouse(warehouse)
    simulate_robot(warehouse, moves, part == 2)
    print(f"Part {part} - Sum of GPS coordinates: {calculate_gps_sum(warehouse, part == 2)}")

if __name__ == "__main__":
    solve(1)
    solve(2)
