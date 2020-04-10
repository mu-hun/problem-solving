import solution from './42746'

describe('[6, 10, 2] will return', () => {
  test('6210', () => {
    expect(solution([6, 10, 2])).toEqual('6210')
  })
})

describe('[3, 30, 34, 5, 9] will return', () => {
  test('9534330', () => {
    expect(solution([3, 30, 34, 5, 9])).toEqual('9534330')
  })
})
