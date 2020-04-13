import { solution } from './42862'

const testCases = [
  [5, [2, 4], [1, 3, 5]],
  [5, [2, 4], [3]],
  [3, [3], [1]],
  [7, [2, 4], [3, 6]],
  [5, [2, 5], [1, 3, 5]],
] as [number, number[], number[]][]

test(testCases[0].join(' | '), () => {
  expect(solution(...testCases[0])).toBe(5)
})
test(testCases[1].join(' | '), () => {
  expect(solution(...testCases[1])).toBe(4)
})
test(testCases[2].join(' | '), () => {
  expect(solution(...testCases[2])).toBe(2)
})
test(testCases[3].join(' | '), () => {
  expect(solution(...testCases[3])).toBe(6)
})
test(testCases[4].join(' | '), () => {
  expect(solution(...testCases[4])).toBe(5)
})
