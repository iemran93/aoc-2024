# another approach for d4
import sys

#(row, col) direction offset
directions= [
    (-1, 0), (0, -1),
    (0, -1), (0, 1),
    (-1, -1), (-1, 1,),
    (1, -1), (1, 1)
]

def part1(lines):
 # dynamic traversal => include the i of the word and the direction offset
 
 pass

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Provide the data file!")
        sys.exit(1)

    data_path = args[0]

    lines = []

    with open(data_path, "r") as file:
        for line in file:
            lines.append(line.strip())
    print("Part1 solution: ", part1(lines))
    # print("Part2 solution: ", part2(lines))