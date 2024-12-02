# The input consists of many reports, one report per line. 
# Each report is a list of numbers called levels that are separated by spaces.


def main():
    input_path = "input.txt"

    reports = format_reports(input_path)

    safe = 0

    for i in reports.keys():
        if is_safe(reports[i]):
            safe += 1

    print(safe)

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

    # First check first and second elements to set whether its increasing or decreasing
    if report[0] < report[1]:
         increasing = True
         jump = abs(report[1] - report[0])
         if jump > 3 or jump < 1:
            return False
    elif report[0] == report[1]:
        return False # immediately return false here because this means list isn't increasing or decreasing
    else:
        increasing = False
        jump = abs(report[1] - report[0])
        if jump > 3 or jump < 1:
            return False

    if increasing:
        for i in range(1, len(report)-1): # start from by comparing 1 -> 2, we already checked 0 -> 1
            jump = abs(report[i] - report[i+1])
            if report[i] > report[i+1] or report[i] == report[i+1]:
                return False
            elif jump > 3 or jump < 1:
                return False
    else: # decreasing
        for i in range(1, len(report)-1): # start from by comparing 1 -> 2, we already checked 0 -> 1
            jump = abs(report[i] - report[i+1])
            if report[i] < report[i+1] or report[i] == report[i+1]:
                return False
            elif jump > 3 or jump < 1:
                return False
            
    return True


if __name__ == "__main__":
    main()