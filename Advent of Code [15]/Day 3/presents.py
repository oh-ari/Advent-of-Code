# movement!
MOVES = {
    '^': (0, 1),   # North
    'v': (0, -1),  # South
    '>': (1, 0),   # East
    '<': (-1, 0)   # West
}

def santa_presents(directions):
    x, y = 0, 0
    visited = {(0, 0)}
    # processing the directions here:
    for direction in directions:
        dx, dy = MOVES[direction]
        x += dx
        y += dy
        visited.add((x, y))

    return len(visited)

def robot_presents(directions):
    positions = [(0, 0), (0, 0)]
    visited = {(0, 0)}

    for i, direction in enumerate(directions):
        x, y = positions[i % 2]
        dx, dy = MOVES[direction]
        positions[i % 2] = (x + dx, y + dy)
        visited.add(positions[i % 2])

    return len(visited)
# reading the input as always:
with open('input.txt', 'r') as file:
    directions = file.read().strip()

# then we can get the results and print em
result1 = santa_presents(directions)
result2 = robot_presents(directions)
print(f"houses with at least one present (just santa): {result1}")
print(f"houses with at least one present (santa and robot santa): {result2}")
