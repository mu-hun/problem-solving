export default function solution(numbers: number[], target: number) {
  const go = (index: number, cnt: number): number => {
    if (index == numbers.length) {
      if (cnt == target) return 1
      return 0
    }
    return (
      go(index + 1, cnt + numbers[index]) + go(index + 1, cnt - numbers[index])
    )
  }

  return go(0, 0)
}
