from heapq import heappush, heappop
from dataclasses import dataclass
from typing import Tuple, Set, Dict
from collections import defaultdict

@dataclass(frozen=True)
class State:
    pos: Tuple[int, int]  # y x
    direction: Tuple[int, int]  # dy dx

def read_maze(filename: str) -> tuple[list[str], tuple[int, int], tuple[int, int]]:
    maze = []
    start = end = None
    with open(filename) as f:
        for y, line in enumerate(f):
            row = line.strip()
            maze.append(row)
            if 'S' in row: start = (y, row.index('S'))
            if 'E' in row: end = (y, row.index('E'))
    return maze, start, end

def get_neighbors(state: State, maze: list[str]) -> list[tuple[State, int]]:
    neighbors = []
    y, x = state.pos
    dy, dx = state.direction
    
    # rotate left and right
    for new_dy, new_dx in [(-dx, dy), (dx, -dy)]:
        neighbors.append((State((y, x), (new_dy, new_dx)), 1000))
    
    # move forward
    new_y, new_x = y + dy, x + dx
    if (0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]) and 
        maze[new_y][new_x] != '#'):
        neighbors.append((State((new_y, new_x), (dy, dx)), 1))
    
    return neighbors

def find_optimal_paths(maze: list[str], start: tuple[int, int], end: tuple[int, int]) -> tuple[int, set]:
    initial_state = State(start, (0, 1))
    counter = 0  # unique counter for heap ordering
    queue = [(0, 0, counter, initial_state)]
    visited = {}  # state to score map
    g_scores = {initial_state: 0}
    came_from = defaultdict(set)  # track multiple paths
    min_score = float('inf')
    
    while queue:
        _, g_score, _, current = heappop(queue)
        
        if current.pos == end:
            min_score = min(min_score, g_score)
            continue
        
        if current in visited and g_score > visited[current]: continue
        visited[current] = g_score
        
        for next_state, cost in get_neighbors(current, maze):
            new_g_score = g_score + cost
            
            if new_g_score > min_score: continue
                
            if next_state not in g_scores or new_g_score <= g_scores[next_state]:
                if new_g_score == g_scores.get(next_state, float('inf')):
                    came_from[next_state].add(current)
                else:
                    g_scores[next_state] = new_g_score
                    came_from[next_state] = {current}
                
                counter += 1
                f_score = new_g_score + abs(next_state.pos[0] - end[0]) + abs(next_state.pos[1] - end[1])
                heappush(queue, (f_score, new_g_score, counter, next_state))
    
    # build all optimal paths
    optimal_tiles = set()
    def trace_path(state, path_tiles):
        if state.pos == start:
            path_tiles.add(start)
            return
        path_tiles.add(state.pos)
        for prev in came_from[state]:
            trace_path(prev, path_tiles)
    
    # collect tiles from optimal paths
    for state in g_scores:
        if state.pos == end and g_scores[state] == min_score:
            path_tiles = set()
            trace_path(state, path_tiles)
            optimal_tiles.update(path_tiles)
    
    return min_score, optimal_tiles

def solve():
    maze, start, end = read_maze("input.txt")
    min_score, optimal_tiles = find_optimal_paths(maze, start, end)
    print(f"Part 1 - Lowest possible score: {min_score}")
    print(f"Part 2 - Number of tiles in optimal paths: {len(optimal_tiles)}")

if __name__ == "__main__":
    solve()
