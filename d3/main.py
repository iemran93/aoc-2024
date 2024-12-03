import sys
import re


def part1(lines):
    total = 0
    for line in lines:
        section = ""
        for i, chr in enumerate(line):
            if chr == "m":
                section = line[i:i+12]
            # check if this section can have this substring mul(x,y), x and y are integers of 1 to 3 digits max
            # if yes, return the product of x and y
            # else return 0
                pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
                # g1&g2 = (\d{1,3})
                match = re.match(pattern, section)
                if match:
                    print(section)
                    x = int(match.group(1))
                    y = int(match.group(2))
                    total += x * y

    return total


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Provide the data file!")
        sys.exit(1)

    data_path = args[0]

    lines = []

    with open(data_path, "r") as file:
        for line in file:
            lines.append(line)
    print("part1 sol: ", part1(lines))
    # print("part2 sol: ", part2(reports))
