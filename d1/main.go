package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
	"time"
)

func main() {
	start := time.Now()
	args := os.Args
	if len(args[1:]) != 1 {
		log.Fatal("Provide the data file!")
	}
	file_path := args[1]

	rside, lside := readFile(file_path)

	fmt.Println("part1 sol: ", part1(rside, lside))
	// fmt.Println("part2 sol: ", part2(rside, lside))

	elapsed := time.Since(start)
	fmt.Printf("\nexec took: %v\n", elapsed)
}

func part1(rside, lside []int) int {
	var total float64

	sort.Slice(rside, func(i, j int) bool {
		return rside[i] < rside[j]
	})
	sort.Slice(lside, func(i, j int) bool {
		return lside[i] < lside[j]
	})

	for i := range rside {
		total += math.Abs(float64(rside[i] - lside[i]))
	}
	return int(total)
}

func part2(rside, lside []int) int {
	var seen = make(map[int]int)
	var total int
	for _, i := range rside {
		if _, exist := seen[i]; exist {
			total += seen[i]
			continue
		}
		var count int
		for _, j := range lside {
			if i == j {
				count += 1
			}
		}
		seen[i] = i * count
		total += seen[i]
	}
	return total
}

func readFile(file_path string) ([]int, []int) {
	file, err := os.Open(file_path)
	if err != nil {
		log.Fatal("Error reading the file!")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var rside, lside []int
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		rsideV, err := strconv.Atoi(parts[0])
		if err != nil {
			log.Fatal("Error converting to int", err)
		}
		rside = append(rside, rsideV)
		lsideV, err := strconv.Atoi(parts[1])
		if err != nil {
			log.Fatal("Error converting to int", err)
		}
		lside = append(lside, lsideV)
	}
	return rside, lside
}
