from dataclasses import dataclass
from typing import Optional
from sympy import Eq, solve, symbols
from sympy.core.numbers import Integer

@dataclass
class Point:
    x: int
    y: int

def find_solution_math(button_a: tuple[int, int], button_b: tuple[int, int], 
                      prize: tuple[int, int], part2: bool = False) -> int:
    # setup points
    a, b, t = Point(*button_a), Point(*button_b), Point(*prize)
    
    # part 2 offset
    if part2:
        t.x += 10**13
        t.y += 10**13
    
    try:
        # solve system
        m, n = symbols('m n')
        solution = solve((
            Eq(a.x * m + b.x * n, t.x),
            Eq(a.y * m + b.y * n, t.y)
        ), (m, n))
        
        # check valid int solution
        if solution and all(isinstance(val, Integer) for val in solution.values()):
            m_val, n_val = int(solution[m]), int(solution[n])
            if m_val >= 0 and n_val >= 0:
                return m_val * 3 + n_val
    except:
        pass
    return 0

def solve_puzzle(input_data: str, part2: bool = False) -> int:
    # parse input
    lines = [line for line in input_data.strip().split('\n') if line.strip()]
    total = 0
    
    # process machines
    for i in range(0, len(lines), 3):
        if i + 2 >= len(lines): break
        
        # get coords
        coords = []
        for line in lines[i:i+3]:
            parts = line.split(': ')[1].split(', ')
            coords.append((int(parts[0][2:]), int(parts[1][2:])))
        
        # add solution
        total += find_solution_math(*coords, part2)
    
    return total

# read and solve
with open('input.txt', 'r') as f:
    data = f.read()

print(f"Part 1: {solve_puzzle(data, False)}")
print(f"Part 2: {solve_puzzle(data, True)}")
