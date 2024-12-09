from itertools import product
import operator

# Part 1
# Each line represents a single equation. 
# The test value appears before the colon on each line; 
# it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.
# Operators are always evaluated left-to-right, not according to precedence rules. 
# Furthermore, numbers in the equations cannot be rearranged. 
# Only two different types of operators: add (+) and multiply (*).
# Return the sum of the test values from just the equations that could possibly be true.

# Part 2
# The concatenation operator (||) combines the digits from its left and right inputs into a single number. 
# For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.
# Add this operator and again return the sum of the test values from the equations that could possibly be true.





def get_possible_answers(text: str):
    lines = text.strip().split("\n")
    possible = []

    for line in lines:
        parts = line.split()
        answer = int(parts[0].replace(":", ""))
        operands = [int(x) for x in parts[1:]]
        if calculable(answer, operands):
            possible.append(answer)

    return possible

def concatenate(a, b):
    return int(str(a) + str(b))


def calculable(answer: int, operands: list):

    num_of_operators = len(operands) - 1

    operator_map = {
        "+": operator.add,
        "*": operator.mul,
        "||": concatenate
    }

    operators = operator_permutations(num_of_operators)

    for combination in operators:
        result = operands[0]
        for i in range(len(combination)):
            op = combination[i]
            func = operator_map[op]
            result = func(result, operands[i + 1])
        if result == answer:
            return True

    return False

def operator_permutations(num: int):
    operators = ["*", "+", "||"]
    return list(product(operators, repeat=num))

def main():
    with open("input.txt", "r") as file:
        text = file.read()

    possible_answers = get_possible_answers(text)
    
    total = 0
    for possible in possible_answers:
        total += possible

    print(total)


if __name__ == "__main__":
    main()
