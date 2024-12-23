# Part 1:
# Pair up the smallest number in the left list with the smallest number in the right list,
# then the second-smallest left number with the second-smallest right number, and so on.

# Within each pair, figure out how far apart the two numbers are; 
# you'll need to add up all of those distances. 
# For example, if you pair up a 3 from the left list with a 7 from the right list, 
# the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

# Part 2:
# This time, you'll need to figure out exactly how often each number from the left list appears in the right list. 
# Calculate a total similarity score by adding up each number in the left list a
# after multiplying it by the number of times that number appears in the right list.

def main():
    input_path = "input.txt"
    list1, list2 = format_lists(input_path)

    list1.sort()
    list2.sort()

    distances = get_distances(list1, list2)

    similarity = similarity_score(list1, list2)

    print(similarity)

def similarity_score(list1: list, list2: list):

    total = 0
    list2_counts = {}

    for number in list2:
        if number not in list2_counts:
            list2_counts[number] = 1
        else:
            list2_counts[number] += 1

    for i in range(0, len(list1)):
        if list1[i] in list2:
            total += (list2_counts[list1[i]] * list1[i])

    return total
    
def get_distances(list1: list, list2: list):
    distances = []

    for i in range(0, len(list1)):
        distances.append(abs(list1[i] - list2[i]))
    
    return distances

def format_lists(file_path: str):
    list1 = []
    list2 = []

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            list1.append(int(parts[0]))
            list2.append(int(parts[1]))
            
    return list1, list2

if __name__ == "__main__":
    main()