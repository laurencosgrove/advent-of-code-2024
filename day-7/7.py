from itertools import product
import operator


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

def calculable(answer: int, operands: list):

    num_of_operators = len(operands) - 1

    operator_map = {
        "+": operator.add,
        "*": operator.mul,
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
    operators = ["*", "+"]
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
