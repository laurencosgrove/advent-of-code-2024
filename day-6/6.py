# Part 1
# The map shows the current position of the guard with ^ 
# (to indicate the guard is currently facing up from the perspective of the map). 
# Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

# Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
    # If there is something directly in front of you, turn right 90 degrees.
    # Otherwise, take a step forward.

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

def obstacle_ahead(lines: list, x: str, y: str, direction: str):

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

def new_position(x: str, y: str, direction: str):

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
    with open("input.txt", "r") as file:
        text = file.read()

    lines = text.strip().split('\n')

    lines = [list(x) for x in lines]

    move_count = 0
    while on_map(lines):
        move_count += 1
    
    total = 0
    for line in lines:
        # count Xs
        total += line.count('X')
        print("".join(line))
    
    # add one for the final guard position
    print(total+1)


if __name__ == "__main__":
    main()


