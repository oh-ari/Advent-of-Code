import re

def corruption(input_text, with_conditionals=False):
    # patterns for instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # find all instructions with their positions
    instructions = []
    
    # find multiplications
    for match in re.finditer(mul_pattern, input_text):
        instructions.append(('mul', match.start(), 
                           int(match.group(1)), int(match.group(2))))
    
    if with_conditionals:
        # find do() and don't() instructions
        for match in re.finditer(do_pattern, input_text):
            instructions.append(('do', match.start()))
        for match in re.finditer(dont_pattern, input_text):
            instructions.append(('dont', match.start()))
        
        # sort instructions by position
        instructions.sort(key=lambda x: x[1])
    
    # process instructions
    enabled = True  # start with multiplications enabled
    total = 0
    
    for inst in instructions:
        if with_conditionals:
            if inst[0] == 'do':
                enabled = True
            elif inst[0] == 'dont':
                enabled = False
            elif inst[0] == 'mul' and enabled:
                total += inst[2] * inst[3]
        else:
            if inst[0] == 'mul':
                total += inst[2] * inst[3]
    
    return total

# read input and solve both parts
with open('input.txt', 'r') as f:
    input_text = f.read()

part1_result = corruption(input_text)
part2_result = corruption(input_text, with_conditionals=True)

print(f"Sum of all multiplication results: {part1_result}")
print(f"Sum of enabled multiplication results: {part2_result}")
