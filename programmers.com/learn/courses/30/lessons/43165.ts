export default function solution(numbers: number[], target: number) {
  return go([], 0, numbers, target)
}

const difference = (array: number[], n: number) =>
  [...new Array(n).keys()].filter(x => !array.includes(x))

const go = (
  array: number[],
  index: number,
  numbers: number[],
  target: number
): number => {
  if (index == numbers.length) {
    let cnt = 0
    for (const i in array) cnt += numbers[i]
    for (const i in difference(array, numbers.length)) cnt -= numbers[i]
    if (cnt == target) return 1
    return 0
  }
  return (
    go([...array, index], index + 1, numbers, target) +
    go(array, index + 1, numbers, target)
  )
}
