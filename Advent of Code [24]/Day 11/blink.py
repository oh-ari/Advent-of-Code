from functools import lru_cache

def stone(n):
    # if zero, make it 1
    if n == 0:
        return [1]
    # even number of digits? split it in half
    elif len(str(n)) % 2 == 0:
        mid = len(str(n)) // 2
        return [int(str(n)[:mid]), int(str(n)[mid:])]
    # otherwise multiply by 2024
    return [n * 2024]

@lru_cache(maxsize=None)
def blink(n, iterations):
    products = stone(n)
    if iterations == 0:
        return len(products)
    return sum(blink(s, iterations - 1) for s in products)

def solve(input_file, blinks):
    # grab numbers from file
    with open(input_file) as f:
        stones = [int(x) for x in f.read().strip().split()]
    return sum(blink(stone, blinks - 1) for stone in stones)

if __name__ == "__main__":
    p1, p2 = solve("input.txt", 25), solve("input.txt", 75)
    print(f"part 1: {p1}\npart 2: {p2}")
