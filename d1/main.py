import sys
import time
from collections import Counter


def part1(rside, lside):
    rside.sort()
    lside.sort()
    total = 0
    for i in range(len(rside)):
        total += abs(rside[i] - lside[i])
    return total


def part2(rside, lside):
    total = 0
    seen = {}
    for i in rside:
        if i in seen.keys():
            total += seen[i]
            continue
        count = 0
        for j in lside:
            if i == j:
                count += 1
        seen[i] = i * count
        total += seen[i]
    return total


if __name__ == "__main__":
    start_time = time.time()
    args = sys.argv[1:]
    if len(args) != 1:
        print("Provide the data file!")
        sys.exit(1)

    data_path = args[0]

    rside = []
    lside = []

    with open(data_path, "r") as file:
        for line in file:
            parts = line.split()
            rside.append(int(parts[0]))
            lside.append(int(parts[1]))

    print("part1 sol: ", part1(rside, lside))
    # print("part2 sol: ", part2(rside, lside))
    # print("exec took: ", time.time()-start_time)
