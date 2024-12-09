# another approach for d4
import sys

# (row, col) direction offset
directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

word = "XMAS"


def sol(lines):
    count = 0
    count2 = 0
    # dynamic traversal => include the i of the word and the direction offset
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "A":
                # boundry checking
                if 1 <= row < len(lines) - 1 and 1 <= col < len(lines[row]) - 1:
                    diag1 = (
                        lines[row - 1][col - 1]
                        + lines[row][col]
                        + lines[row + 1][col + 1]
                    ) in ["MAS", "SAM"]
                    diag2 = (
                        lines[row - 1][col + 1]
                        + lines[row][col]
                        + lines[row + 1][col - 1]
                    ) in ["MAS", "SAM"]
                    if diag1 and diag2:
                        count2 += 1

            for dr, dc in directions:
                if 0 <= row + (len(word) - 1) * dr < len(lines) and 0 <= col + (
                    len(word) - 1
                ) * dc < len(lines[row]):
                    sequence = "".join(
                        lines[row + i * dr][col + i * dc] for i in range(len(word))
                    )
                    if sequence == word:
                        count += 1

    return count, count2


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
    p1, p2 = sol(lines)
    print(f"p1 sol: {p1}\np2 sol: {p2}\n")
