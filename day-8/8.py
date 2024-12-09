def count_antinodes(text: str):

    cells = [list(line.strip()) for line in text.strip().split("\n")]

    height = len(cells)
    width = len(cells[0])

    empty = "."
    antennas = {}

    for row in range(height):
        for col in range(width):
            if cells[row][col] != empty:
                if cells[row][col] not in antennas:
                    antennas[cells[row][col]] = []
                antennas[cells[row][col]].append([row, col])

    antinodes = set()

    for coordinates in antennas.values():
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                gap = [coordinates[j][0] - coordinates[i][0], coordinates[j][1] - coordinates[i][1]]

                for index, direction in [(i, -1), (j, 1)]:

                    new_position = [
                        coordinates[index][0] + gap[0] * direction,
                        coordinates[index][1] + gap[1] * direction
                    ]
                    
                    # check if it's on the map
                    if 0 <= new_position[0] < height and 0 <= new_position[1] < width:
                        antinodes.add(tuple(new_position)) 

    return len(antinodes)

def main():
    with open("input.txt", "r") as file:
        text = file.read()

    print(count_antinodes(text))

if __name__ == "__main__":
    main()
