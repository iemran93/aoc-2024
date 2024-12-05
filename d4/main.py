import sys

word = "XMAS"

def get_status(lines, row, col):
    status = {
        "up": False, "down": False, 
        "left": False, "right": False,
        "up-left": False, "up-right": False,
        "down-left": False, "down-right": False
    }
    if row >= len(word)-1:
        status["up"] = True
    if row + len(word) <= len(lines):
        status["down"] = True
    if col >= len(word)-1:
        status["left"] = True
    if col + len(word) <= len(lines[row]):
        status["right"] = True
    if row >= len(word)-1 and col >= len(word)-1:
        status["up-left"] = True
    if row >= len(word)-1 and col + len(word) <= len(lines[row]):
        status["up-right"] = True
    if row + len(word) <= len(lines) and col >= len(word)-1:
        status["down-left"] = True
    if row + len(word) <= len(lines) and col + len(word) <= len(lines[row]):
        status["down-right"] = True
    return status

def part1(lines):
    count = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "X":
                square_status = get_status(lines, row, col)
                
                if square_status["up"]:
                    if "".join([lines[row-i][col] for i in range(len(word))]) == word:
                        count += 1
                if square_status["down"]:
                    if "".join([lines[row+i][col] for i in range(len(word))]) == word:
                        count += 1
                if square_status["left"]:
                    if "".join([lines[row][col-i] for i in range(len(word))]) == word:
                        count += 1
                if square_status["right"]:
                    if "".join([lines[row][col+i] for i in range(len(word))]) == word:
                        count += 1
                if square_status["up-left"]:
                    if "".join([lines[row-i][col-i] for i in range(len(word))]) == word:
                        count += 1
                if square_status["up-right"]:
                    if "".join([lines[row-i][col+i] for i in range(len(word))]) == word:
                        count += 1
                if square_status["down-left"]:
                    if "".join([lines[row+i][col-i] for i in range(len(word))]) == word:
                        count += 1
                if square_status["down-right"]:
                    if "".join([lines[row+i][col+i] for i in range(len(word))]) == word:
                        count += 1
    return count

def part2(lines):
    count = 0
    for row in range(1, len(lines) - 1):
        for col in range(1, len(lines[row]) - 1):
            if (
                (lines[row - 1][col - 1] == "M" and
                 lines[row][col] == "A" and
                 lines[row + 1][col + 1] == "S") or
                (lines[row - 1][col - 1] == "S" and
                 lines[row][col] == "A" and
                 lines[row + 1][col + 1] == "M")
            ):
                if (
                    (lines[row - 1][col + 1] == "M" and
                     lines[row][col] == "A" and
                     lines[row + 1][col - 1] == "S") or
                    (lines[row - 1][col + 1] == "S" and
                     lines[row][col] == "A" and
                     lines[row + 1][col - 1] == "M")
                ):
                    count += 1
    return count


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
    print("Part2 solution: ", part2(lines))
