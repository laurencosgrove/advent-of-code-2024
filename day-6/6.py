# Part 1
# The map shows the current position of the guard with ^ 
# (to indicate the guard is currently facing up from the perspective of the map). 
# Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

# Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
    # If there is something directly in front of you, turn right 90 degrees.
    # Otherwise, take a step forward.

# Part 2
# Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. 
# They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, 
# making the rest of the lab safe to search.
# To have the lowest chance of creating a time paradox, 
# The Historians would like to know all of the possible positions for such an obstruction. 
# The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

def place_obstacle(lines: list, x: int, y: int, direction: str):
    height = len(lines)
    width = len(lines[0])
    possible_positions = []

    for i in range(height):
        for j in range(width):
            # skip if guard is there or theres alraeady an obstacle
            if (j == x and i == y) or lines[i][j] == "#":
                continue
            
            original = lines[i][j]
            lines[i][j] = "#"

            if causes_loop(lines, x, y, direction):
                possible_positions.append((j, i))

            lines[i][j] = original

    return possible_positions

def causes_loop(lines: list, x: int, y: int, direction: str):
    height = len(lines)
    width = len(lines[0])
        
    # track visited states
    visited = set()
    
    # if we ever visit the same position twice, we're in a loop
    while True:
        position = (x, y, direction)
        
        if position in visited:
            return True
        
        visited.add(position)
        
        if obstacle_ahead(lines, x, y, direction):
            direction = rotate_90(direction)
        else:
            new_x, new_y = new_position(x, y, direction)
            
            if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                return False
            
            if lines[new_y][new_x] == "#":
                return False
            
            # update guard's position
            x, y = new_x, new_y


def on_map(lines: list):
    height = len(lines)
    width = len(lines[0])

    # find position of the guard
    x, y, direction = find_guard(lines)

    if obstacle_ahead(lines, x, y, direction):
        lines[y][x] = rotate_90(direction)
    else:
        # try to move in the direction we're facing
        new_x, new_y = new_position(x, y, direction)
        # check if either of these are off of the map
        if new_x >= width or new_x < 0 or new_y >= height or new_y < 0:
            return False
        
        # put the guard in the new position
        lines[new_y][new_x] = direction

        # remove the guard from the old position and mark it with an X
        lines[y][x] = "X"

    return True

def find_guard(lines: list):
    height = len(lines)
    width = len(lines[0])

    for i in range(height):
        for j in range(width):
            for direction in ["^", ">", "v", "<"]:
                if lines[i][j] == direction:
                    return j, i, direction
    
    return None, None, None

def rotate_90(direction: str):
    if direction == "^":
        return ">"
    elif direction == ">":
        return "v"
    elif direction == "v":
        return "<"
    elif direction == "<":
        return "^"
    else:
        print(f"error: invalid direction! {direction}")
    
    return None

def obstacle_ahead(lines: list, x: int, y: int, direction: str):

    height = len(lines)
    width = len(lines[0])

    if direction == "^":
        # check y - 1
        if y - 1 >= 0:
            if lines[y-1][x] == "#":
                return True
    elif direction == "v":
        # check y + 1
        if y + 1 < height:
            if lines[y+1][x] == "#":
                return True
    elif direction == ">":
        # check x + 1
        if x + 1 < width:
            if lines[y][x+1] == "#":
                return True
    elif direction == "<":
        # check x - 1
        if x - 1 >= 0: 
            if lines[y][x-1] == "#":
                return True
    else:
        print(f"error: invalid direction! {direction}")

    return False

def new_position(x: int, y: int, direction: str):

    if direction == "^":
        # move upwards
        y -= 1
    elif direction == "v":
        y += 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    else:
        print(f"error: invalid direction! {direction}")

    return x, y


def main():
    with open("test-input.txt", "r") as file:
        text = file.read()

    lines = text.strip().split('\n')
    lines = [list(x) for x in lines]

    # Part 1

    original_lines = [row[:] for row in lines]  # copy the map to use in part 2
    move_count = 0
    while on_map(lines):
        move_count += 1

    total = 0
    for line in lines:
        # count Xs
        total += line.count('X')
    
    # add one for the final guard position
    print(f"Total moves: {total + 1}")

    # Part 2

    x, y, direction = find_guard(original_lines)
    possible_positions = place_obstacle(original_lines, x, y, direction) 
    
    # Print results
    print(f"Possible positions: {len(possible_positions)}")

if __name__ == "__main__":
    main()


