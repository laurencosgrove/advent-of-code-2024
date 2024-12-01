# Pair up the smallest number in the left list with the smallest number in the right list,
# then the second-smallest left number with the second-smallest right number, and so on.

# Within each pair, figure out how far apart the two numbers are; 
# you'll need to add up all of those distances. 
# For example, if you pair up a 3 from the left list with a 7 from the right list, 
# the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

import os

def main():
    input_path = "input.txt"
    list1, list2 = format_lists(input_path)

    # sort lists

    list1.sort()
    list2.sort()

    distances = get_distances(list1, list2)

    print(sum(distances))

def get_distances(list1: list, list2: list):
    distances = []

    for i in range(0, len(list1)):
        distances.append(abs(list1[i] - list2[i]))
    
    return distances


def format_lists(file_path: str):
    list1 = []
    list2 = []


    text = open(file_path, "r")

    for line in text:
        parts = line.split("   ")
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))
        
    return list1, list2

if __name__ == "__main__":
    main()