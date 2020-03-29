import solution from './43162'

const examples = [
  {
    n: 3,
    computers: [
      [1, 1, 0],
      [1, 1, 0],
      [0, 0, 1]
    ],
    return: 2
  },
  {
    n: 3,
    computers: [
      [1, 1, 0],
      [1, 1, 1],
      [0, 1, 1]
    ],
    return: 1
  }
]

describe('network: DFS', () => {
  examples.forEach(example => {
    describe(`${example.n} computer, ${example.computers} will return`, () => {
      test(`${example.return}`, () => {
        expect(solution(example.n, example.computers)).toBe(example.return)
      })
    })
  })
})
