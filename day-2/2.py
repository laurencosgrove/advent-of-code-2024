# Part 1
# The input consists of many reports, one report per line. 
# Each report is a list of numbers called levels that are separated by spaces.
# Criteria for a safe report:
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.

# Part 2
# Now, the same rules apply as before, except if removing a single level 
# from an unsafe report would make it safe, the report instead counts as safe.


def main():
    input_path = "input.txt"

    reports = format_reports(input_path)

    print(one_level_away(reports))


def format_reports(file_path: str):
    reports = {}
    counter = 0

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            reports[counter] = parts
            counter += 1
    return reports

def is_safe(report: list):
    # Criteria:
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.

    report = [ int(x) for x in report]

    # First check first and second elements to set whether it's increasing or decreasing
    increasing = report[0] < report[1]

    # for the rest of the elements
    for i in range(len(report) - 1):
        jump = report[i + 1] - report[i]
        if jump == 0 or abs(jump) > 3 or (increasing and jump < 0) or (not increasing and jump > 0):
            return False

    return True

def one_level_away(reports: dict):
    safe = 0
    for report in reports.values():
        if is_safe(report) or is_safe_bar_one(report):
            safe += 1

    return safe
                
def is_safe_bar_one(report: list):
    for i in range(len(report)): 
        removed_item = report[i]  # save the element to remove
        del report[i]  
        if is_safe(report):
            return True
        report.insert(i, removed_item)  # restore the removed element
    return False 


     
if __name__ == "__main__":
    main()