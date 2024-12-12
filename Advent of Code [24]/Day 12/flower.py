from collections import deque

def get_whole_plot(plant, pos, plots, limits, found):
    x, y = pos
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        new_x = x + dx
        new_y = y + dy

        if (new_x, new_y) not in found:
            if all(p in lim for p, lim in zip([new_x, new_y], limits)):
                if plots[new_y][new_x] == plant:
                    new_pos = (new_x, new_y)
                    found.add(new_pos)
                    found.update(get_whole_plot(plant, new_pos, plots, limits, found))
    return found

def get_num_neighbours(pos, plot):
    num = 0
    x, y = pos
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        if (x + dx, y + dy) in plot:
            num += 1
    return num

def get_plant(x, y, plots, plot, limits):
    if all(p in lim for p, lim in zip([x, y], limits)):
        if (x, y) in plot:
            return plots[y][x]
    return None

def solve(input_text):
    # parse input
    plots = [list(line) for line in input_text.splitlines()]
    max_x = len(plots[0])
    max_y = len(plots)
    limits = [range(max_x), range(max_y)]
    
    # find all regions
    visited = set()
    plots_identified = {}
    for y in limits[1]:
        for x in limits[0]:
            start = (x, y)
            if start not in visited:
                plant = plots[y][x]
                found = set()
                found.add(start)
                found = get_whole_plot(plant, (x, y), plots, limits, found)
                plots_identified[start] = found
                visited.update(found)

    # calculate part 1 (perimeter)
    part1_regions = []
    for plot in plots_identified.values():
        area = len(plot)
        perimeter = 0
        for x, y in plot:
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) not in plot:
                    perimeter += 1
        part1_regions.append((area, perimeter))
    
    # calculate part 2 (distinct sides)
    part2_regions = []
    diagonals = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for plot in plots_identified.values():
        num_lines = 0
        for pos in plot:
            num_neighbours = get_num_neighbours(pos, plot)
            if num_neighbours == 0:
                num_lines += 4
            elif num_neighbours == 1:
                num_lines += 2
            else:
                x, y = pos
                plant = plots[y][x]
                for dx, dy in diagonals:
                    new_x = x + dx
                    new_y = y + dy

                    diagonal_plant = get_plant(new_x, new_y, plots, plot, limits)
                    plant1 = get_plant(new_x, y, plots, plot, limits)
                    plant2 = get_plant(x, new_y, plots, plot, limits)

                    if diagonal_plant != plant:
                        if plant1 == plant and plant2 == plant:
                            num_lines += 1
                        elif plant1 != plant and plant2 != plant:
                            num_lines += 1
                    elif plant1 != plant and plant2 != plant:
                        num_lines += 1
        part2_regions.append((len(plot), num_lines))

    part1 = sum(area * perim for area, perim in part1_regions)
    part2 = sum(area * sides for area, sides in part2_regions)
    
    return part1, part2

with open('input.txt') as f:
    input_text = f.read()
    
p1, p2 = solve(input_text)
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
