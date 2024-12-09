def parse_disk_map(s):
    # turn input string into list of file ids and dots
    blocks, id = [], 0
    nums = [int(c) for c in s.strip()]
    for i in range(0, len(nums), 2):
        blocks.extend([id] * nums[i] + ['.'] * (nums[i+1] if i+1 < len(nums) else 0))
        id += 1
    return blocks

def compact_disk_part1(b):
    # move blocks one by one from right to left
    while '.' in b:
        fs = b.index('.')
        lf = next((i for i in range(len(b)-1, fs, -1) if b[i] != '.'), fs)
        if lf <= fs: break
        b[fs], b[lf] = b[lf], '.'

def compact_disk_part2(b):
    # move whole files left, starting with highest id
    for id in range(max(x for x in b if x != '.'), -1, -1):
        # get file positions and size
        pos = [i for i, x in enumerate(b) if x == id]
        if not pos: continue
        size = len(pos)
        
        # find first valid gap
        gap_size = 0
        gap_start = 0
        for i in range(pos[0]):
            if b[i] == '.':
                if gap_size == 0:
                    gap_start = i
                gap_size += 1
                if gap_size >= size:
                    # move file to this gap
                    for p in pos:
                        b[p] = '.'
                    for j in range(size):
                        b[gap_start + j] = id
                    break
            else:
                gap_size = 0

def solve(path):
    # read input and run both parts
    with open(path) as f:
        s = f.read()
    b1, b2 = parse_disk_map(s), parse_disk_map(s)
    compact_disk_part1(b1); compact_disk_part2(b2)
    return [sum(i*x for i,x in enumerate(b) if x != '.') for b in (b1,b2)]

if __name__ == "__main__":
    p1, p2 = solve("input.txt")
    print(f"part 1: {p1}\npart 2: {p2}")
