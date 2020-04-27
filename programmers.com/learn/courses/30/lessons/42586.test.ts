import solution from './42586'

describe('progresses is [93, 30, 55]', () => {
  test('give speeds to [1, 30, 5]', () => {
    expect(solution([93, 30, 55], [1, 30, 5])).toEqual([2, 1])
  })
})
