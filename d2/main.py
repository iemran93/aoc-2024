import sys

def part1(reports):
    safe = []
    for report in reports:
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
    # print("part2 sol: ", part2(reports))