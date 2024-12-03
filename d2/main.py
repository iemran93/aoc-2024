import sys
from itertools import pairwise, combinations

# amazing
# pairwise = s -> (s0,s1), (s1,s2), (s2, s3), ... two pairs of the iterable
# combinations = make a combination of the iterable with the given length
# ^ combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)

min_differ = 1
max_differ = 3


def isSafe1(report):
    # two ture status 1. gradually 2. levels differ
    gradually = report == sorted(
        report) or report == sorted(report, reverse=True)
    differ = all(min_differ <= abs(a-b) <=
                 max_differ for a, b in pairwise(report))
    return gradually and differ


def isSafe2(report):
    for comb in combinations(report, len(report)-1):
        gradually = list(comb) == sorted(
            comb) or list(comb) == sorted(comb, reverse=True)
        differ = all(min_differ <= abs(a-b) <=
                     max_differ for a, b in pairwise(comb))
        if gradually and differ:
            return True
    return False


def part2(reports):
    safe = []
    for report in reports:
        if isSafe2(report):
            safe.append(report)
    return len(safe)


def part1(reports):
    safe = []
    # first approach
    """ for report in reports:
        diff = report[0] - report[1]
        if diff < 0:
            # inc
            added = True
            for i in range(len(report)-1):
                if report[i] - report[i+1] < -3 or report[i] - report[i+1] > -1:
                    added = False
                    break
            if added == True:
                safe.append(report)
        elif diff > 0:
            # dec
            added = True
            for i in range(len(report)-1):
                if report[i] - report[i+1] > 3 or report[i] - report[i+1] < 1:
                    added = False
                    break
            if added == True:
                safe.append(report) """
    # second approach
    for report in reports:
        if isSafe1(report):
            safe.append(report)
    return len(safe)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Provide the data file!")
        sys.exit(1)

    data_path = args[0]

    reports = []

    with open(data_path, "r") as file:
        for line in file:
            report = [int(i) for i in line.split()]
            reports.append(report)
    print("part1 sol: ", part1(reports))
    print("part2 sol: ", part2(reports))
