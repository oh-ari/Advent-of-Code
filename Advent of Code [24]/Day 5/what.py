def parse_rules(rules):
    # create graph of dependencies
    graph = {}
    for rule in rules:
        if '|' in rule:
            before, after = map(int, rule.split('|'))
            graph.setdefault(before, set()).add(after)
    return graph

def is_valid_sequence(seq, graph):
    # check if sequence is valid
    return not any(num2 in graph and num1 in graph[num2] 
                  for i, num1 in enumerate(seq) 
                  for num2 in seq[i+1:])

def order_sequence(seq, graph):
    # sort sequence based on rules
    return sorted(seq, key=lambda x: [y in graph.get(x, set()) for y in seq])

def solve(input_text):
    # process input and calculate totals
    rules, seqs = input_text.strip().split('\n\n')
    rules = [r for r in rules.split('\n') if r]
    seqs = [list(map(int, s.split(','))) for s in seqs.split('\n') if s]
    graph = parse_rules(rules)
    valid_total = invalid_total = 0
    
    for seq in seqs:
        if is_valid_sequence(seq, graph):
            valid_total += seq[len(seq) // 2]
        else:
            invalid_total += order_sequence(seq, graph)[len(seq) // 2]
    return valid_total, invalid_total

# read input and print results
with open('input.txt') as f:
    valid_sum, invalid_sum = solve(f.read())
print("sum of middle numbers for valid sequences:", valid_sum)
print("sum of middle numbers for corrected invalid sequences:", invalid_sum)
