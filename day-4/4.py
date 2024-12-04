def check_rows(lines: list):
    count = 0
    width = len(lines[0])

    for line in lines:
        for i in range(width-3):
            if line[i] == "X" and line[i+1] == "M" and line[i+2] == "A" and line[i+3] == "S":
                count += 1
            elif line[i] == "S" and line[i+1] == "A" and line[i+2] == "M" and line[i+3] == "X":
                count += 1
    return count

def check_cols(lines: list):

    count = 0
    height = len(lines)
    width = len(lines[0])

    for j in range(width):
        for i in range(height - 3):
            if lines[i][j] == "X" and lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
                count += 1
            elif lines[i][j] == "S" and lines[i+1][j] == "A" and lines[i+2][j] == "M" and lines[i+3][j] == "X":
                count += 1
    return count


def check_diagonals(lines: list):
    height = len(lines)
    width = len(lines[0])
    count = 0

    for i in range(height):
        for j in range(width):
            # top left to bottom right
            if i + 3 < height and j + 3 < width:
                if lines[i][j] == "X" and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
                    count += 1
                elif lines[i][j] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M" and lines[i+3][j+3] == "X":
                    count += 1

            # top right to bottom left
            if i + 3 < height and j - 3 >= 0:
                if lines[i][j] == "X" and lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
                    count += 1
                elif lines[i][j] == "S" and lines[i+1][j-1] == "A" and lines[i+2][j-2] == "M" and lines[i+3][j-3] == "X":
                    count += 1
    return count

def find_crosses(lines: list):
    height = len(lines)
    width = len(lines[0])
    count = 0

    for i in range(height):
        for j in range(width):
            # top left to bottom right
            if i + 2 < height and j + 2 < width:
                if lines[i][j] == "M" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "S":
                    # look the opposite way at j + 2
                    if lines[i][j+2] == "M" and lines[i+1][j+1] == "A" and lines[i+2][j] == "S":
                        count += 1
                    elif lines[i][j+2] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j] == "M":
                        count += 1
                # backwards but the same check
                elif lines[i][j] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M":
                     # look the opposite way at j + 2
                    if lines[i][j+2] == "M" and lines[i+1][j+1] == "A" and lines[i+2][j] == "S":
                        count += 1
                    elif lines[i][j+2] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j] == "M":
                        count += 1

    return count


def main():

    with open("input.txt", "r") as file:
        text = file.read()
    
    lines = text.strip().split("\n")
    
    print(f"Down: {check_cols(lines)}")
    print(f"Across: {check_rows(lines)}")
    print(f"Diagonal: {check_diagonals(lines)}")

    total = check_cols(lines) + check_rows(lines) + check_diagonals(lines)

    print(f"Total XMAS: {total}")

    print(f"MAS Crosses: {find_crosses(lines)}")

if __name__ == "__main__":
    main()