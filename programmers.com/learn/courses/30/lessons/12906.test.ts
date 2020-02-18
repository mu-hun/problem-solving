import { solution } from './12906'

const testCases = [
  [1, 1, 3, 3, 0, 1, 1],
  [4, 4, 4, 3, 3]
]

describe('같은 숫자는 싫어', () => {
  test(testCases[0].join(', '), () => {
    expect(solution(testCases[0])).toStrictEqual([1, 3, 0, 1])
  })
  test(testCases[1].join(', '), () => {
    expect(solution(testCases[1])).toStrictEqual([4, 3])
  })
})
