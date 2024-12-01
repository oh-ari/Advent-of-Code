# This is for Part 1, figuring out the distance.
def calculate_distance(left, right):
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))

# This is for Part 2, figuring out the similarity score.
def calculate_similarity(left, right):
    right_counts = {}
    for num in right:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    total_score = 0
    for num in left:
        total_score += num * right_counts.get(num, 0)
    
    return total_score

# Reads the numbers from the file, left and right!
left = []
right = []

with open('numbers.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.strip().split())
        left.append(num1)
        right.append(num2)

print(f"Distance: {calculate_distance(left, right)}")
print(f"Similarity: {calculate_similarity(left, right)}")