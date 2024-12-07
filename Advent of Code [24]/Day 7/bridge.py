def evaluate_expression(nums, ops):
    # start with first num and apply ops left to right
    res = nums[0]
    for i, op in enumerate(ops):
        res = int(str(res) + str(nums[i+1])) if op == '||' else res + nums[i+1] if op == '+' else res * nums[i+1]
    return res

def can_make_target(target, nums, use_concat=False):
    # need at least 2 nums to use operators
    if len(nums) < 2: return False
    
    # set available operators based on part
    ops = ['+', '*', '||'] if use_concat else ['+', '*']
    base = len(ops)
    
    # try all possible operator combinations
    return any(evaluate_expression(nums, 
        [ops[(i // (base ** j)) % base] for j in range(len(nums)-1)])
        == target for i in range(base ** (len(nums)-1)))

def solve_calibration():
    # track totals for both parts
    totals = [0, 0]
    with open('input.txt') as f:
        for line in f:
            # parse target and nums from each line
            target, nums = line.strip().split(':')
            nums = [int(x) for x in nums.split()]
            
            # check both parts
            for i in range(2):
                if can_make_target(int(target), nums, i):
                    totals[i] += int(target)
    return totals

if __name__ == '__main__':
    p1, p2 = solve_calibration()
    print(f"part 1: {p1}\npart 2: {p2}")