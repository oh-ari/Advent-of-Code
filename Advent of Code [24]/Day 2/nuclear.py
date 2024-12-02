def is_safe(levels):
    # here we convert the string into a list of integers
    nums = [int(x) for x in levels.split()]
    # then check the differences between each number
    differences = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    # if the differences are not all positive or all negative, return false
    if not (all(d > 0 for d in differences) or all(d < 0 for d in differences)):
        return False
    # and if the differences are not between 1 and 3, return false
    return all(1 <= abs(d) <= 3 for d in differences)

def is_safe_with_dampener(levels):
    nums = [int(x) for x in levels.split()]
    # if it's already safe, return True
    if is_safe(levels):
        return True
    # try removing each number one at a time
    for i in range(len(nums)):
        # create new list without current number
        dampened_nums = nums[:i] + nums[i+1:]
        # convert back to string format
        dampened_levels = ' '.join(map(str, dampened_nums))
        # check if safe with this number removed
        if is_safe(dampened_levels):
            return True
    return False

# check the file for safe reports
def count_safe(filename):
    safe_count = 0
    dampened_safe_count = 0
    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if is_safe(stripped_line):
                safe_count += 1
                dampened_safe_count += 1
            elif is_safe_with_dampener(stripped_line):
                dampened_safe_count += 1
    return safe_count, dampened_safe_count

# read and process the input file
regular_safe, dampened_safe = count_safe('input.txt')
print(f"Number of safe reports (without dampener): {regular_safe}")
print(f"Number of safe reports (with dampener): {dampened_safe}")
