import { createInterface } from "readline"
import { createReadStream } from "fs"

const rd = createInterface({
  input: createReadStream("data.txt"),
})

let rside = []
let lside = []
rd.on("line", (line) => {
  let parts = line.split(/\s+/)
  lside.push(parseInt(parts[0]))
  rside.push(parseInt(parts[1]))
})

rd.on("close", () => {
  console.log("part1 sol: ", part1(lside, rside))
  //   console.log("part2 sol: ", part2(lside, rside))
})

rd.on("error", (error) => {
  console.error("Error reading file:", error)
})

function part1(lside, rside) {
  lside.sort((a, b) => a - b)
  rside.sort((a, b) => a - b)
  console.log(lside)

  let total = 0
  for (let i = 0; i < lside.length; i++) {
    total += Math.abs(lside[i] - rside[i])
  }

  return total
}

function part2(lside, rside) {}
