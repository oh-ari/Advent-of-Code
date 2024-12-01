def finalfloor(directions):
    return directions.count('(') - directions.count(')')

def basement(directions):
    floor = 0
    
    for pos, char in enumerate(directions, 1):
        floor += 1 if char == '(' else -1
        if floor == -1:
            return pos
    
    return None

# read the input file
with open('input.txt', 'r') as file:
    directions = file.read().strip()

# print the final floor Santa ends up on
final_floor = finalfloor(directions)
print(f"Santa ends up on floor: {final_floor}, huzzah!")

# find when Santa enters the basement and print, as well as print if he doesn't
basement_position = basement(directions)
if basement_position is not None:
    print(f"Santa enters the basement at: {basement_position}")
else:
    print("Santa never enters the basement.")