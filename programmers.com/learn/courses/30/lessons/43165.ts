export default function solution(numbers: number[], target: number) {
  return go(0, 0, numbers, target)
}

const go = (
  index: number,
  cnt: number,
  numbers: number[],
  target: number
): number => {
  if (index == numbers.length) {
    if (cnt == target) return 1
    return 0
  }
  return (
    go(index + 1, cnt + numbers[index], numbers, target) +
    go(index + 1, cnt - numbers[index], numbers, target)
  )
}
