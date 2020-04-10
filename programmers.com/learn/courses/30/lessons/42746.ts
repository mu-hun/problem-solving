export default function solution(numbers: number[]) {
  return numbers.reduce((a, b) => a + b) === 0
    ? '0'
    : numbers.sort(compare).join('')
}

const compare = (a: number, b: number) => (a + '' + b > b + '' + a ? -1 : 1)
