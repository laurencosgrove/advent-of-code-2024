# Part 1

# The goal of the program is just to multiply some numbers. 
# It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. 
# For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. 
# Similarly, mul(123,4) would multiply 123 by 4.
# There are also many invalid characters that should be ignored, 
# even if they look like part of a mul instruction. 
# Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

# Scan the corrupted memory for uncorrupted mul instructions. 
# What do you get if you add up all of the results of the multiplications?

# Part 2

# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies.
# At the beginning of the program, mul instructions are enabled.

import re

def find_muls(text: str):

    pattern = re.compile("mul\(\d+,\d+\)")
    matches = pattern.findall(text)

    return matches

def find_positions(text:str, pattern:str):

    return [(m.end(0)) for m in re.finditer(re.compile(pattern), text)]

def multiply(mul: str):
    mul = mul.replace("mul(", "").replace(")", "")
    numbers = mul.split(",")
    return int(numbers[0]) * int(numbers[1])

def scan(text: str):
    total = 0
    do = True  # do is true initially
    position = 0
    
    while position < len(text):
        if text.startswith("do()", position):
            do = True
            position += 4
        elif text.startswith("don't()", position):
            do = False
            position += 7
        else:
            mul_match = re.match(r"mul\(\d+,\d+\)", text[position:])
            if mul_match:
                if do:
                    total += multiply(mul_match.group(0))
                position += mul_match.end(0)
            else:
                position += 1
    
    return total


def main():

    with open ("input.txt", "r") as file:
        text = file.read()

    print(scan(text))
        

if __name__ == "__main__":
    main()