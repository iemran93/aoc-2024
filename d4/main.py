import sys

word = "XMAS"

def get_status(lines, row, col):
    status = {"up": False, "down": False, "left": False, "right": False}
    if row >= len(word)-1:
        status["up"] = True
    if row + len(word) <= len(lines):
        status["down"] = True
    if col >= len(word)-1:
        status["left"] = True
    if col + len(word) <= len(lines[row]):
        status["right"] = True
    pass

def part1(lines):
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "X":
                square_status = get_status(lines, row, col)
                if square_status["up"] or square_status["down"]:
                     pass
                if square_status["right"] or square_status["left"]:
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
            lines.append(line[:-1])
    print("part2 sol: ", part1(lines))