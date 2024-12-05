# Part 1
# New pages for the safety manuals must be printed in a very specific order:
# The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, 
# page number X must be printed at some point before page number Y
# The input contains both the page ordering rules and the pages to produce in each update
# Start by identifying which updates are already in the right order.
# Within each update, the ordering rules that involve missing page numbers are not used.
# Find the middle page number of each correctly-ordered update.
# What do you get if you add up the middle page number from those correctly-ordered updates?


def parse_input(text: str):
    parts = text.strip().split("\n\n")

    ordering_rules = parts[0].strip().split("\n")
    updates = parts[1].strip().split("\n")

    list_updates = []
    for update in updates:
        list_updates.append(update.strip().split(","))

    return ordering_rules, list_updates

def format_rules(ordering_rules: list):

    formatted_rules = []
    for rule in ordering_rules:
        parts = rule.strip().split("|")
        formatted_rules.append([parts[0], parts[1]])
    
    return formatted_rules


def update_correct(update: list, rules: list):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False  # rule[0] should come before rule[1]
    return True
            
def main():
     # don't need to know full order
     # just need to check whether the updates follow the rules
    with open("input.txt", "r") as file:
        text = file.read()

        rules, updates = parse_input(text)

        rules = format_rules(rules)

        # check what updates are correct
        correct_updates = []
        for update in updates:
            if update_correct(update, rules):
                correct_updates.append(update)
        
        # get the middle value of the update list and add them
        total = 0

        for update in correct_updates:
            middle_index = (len(update) - 1) // 2
            total += int(update[middle_index])

        print(f"Total: {total} ")
if __name__ == "__main__":
    main()