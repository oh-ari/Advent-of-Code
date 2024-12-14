def parse_input(filename):
    # parse pos and vel from each line
    robots = []
    with open(filename, 'r') as f:
        for line in f:
            pos, vel = line.strip().split(' ')
            px, py = map(int, pos[2:].split(','))
            vx, vy = map(int, vel[2:].split(','))
            robots.append(((px, py), (vx, vy)))
    return robots

def update_position(pos, vel, width, height):
    # update pos and wrap around edges
    return ((pos[0] + vel[0]) % width, (pos[1] + vel[1]) % height)

def count_robots(robots, width, height):
    # count robots in each quadrant skip middle lines
    quadrants = [0] * 4
    mid_x, mid_y = width // 2, height // 2
    
    for pos, _ in robots:
        if pos[0] == mid_x or pos[1] == mid_y:
            continue
        quadrant = (2 if pos[1] > mid_y else 0) + (1 if pos[0] > mid_x else 0)
        quadrants[quadrant] += 1
    
    return quadrants

def simulate_robots(robots, width, height, seconds):
    # simulate robot movement for given seconds
    current = robots.copy()
    for _ in range(seconds):
        current = [(update_position(pos, vel, width, height), vel) for pos, vel in current]
    return current

def safety_factor(robots, width, height):
    # multiply number of robots in each quadrant
    result = 1
    for count in count_robots(robots, width, height):
        result *= count
    return result

def message_time(robots, width, height):
    # find when robots form message look for >10 in row
    current = robots.copy()
    for second in range(width * height):
        positions = set(pos for pos, _ in current)
        
        for y in range(height):
            count = max_count = 0
            for x in range(width):
                if (x, y) in positions:
                    count += 1
                else:
                    max_count = max(max_count, count)
                    count = 0
            if max(max_count, count) > 10:
                return second
        
        current = [(update_position(pos, vel, width, height), vel) for pos, vel in current]
        
        if second % 100 == 0:
            print(f"checked {second} seconds...")
    return None

def main():
    width, height = 101, 103
    robots = parse_input('input.txt')
    
    # part 1 safety factor after 100s
    final = simulate_robots(robots, width, height, 100)
    print(f"part 1: {safety_factor(final, width, height)}")
    
    # part 2 find message time
    msg_time = message_time(robots, width, height)
    print(f"part 2: {msg_time if msg_time else 'nope. something went wrong.'}")

if __name__ == "__main__":
    main()
