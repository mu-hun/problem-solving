import solution from './42583'

describe('다리를 지나는 트럭', () => {
  it('첫번째 케이스', () => {
    expect(solution(2, 10, [7, 4, 5, 6])).toBe(8)
  })
  it('두번째 케이스', () => {
    expect(solution(100, 100, [10])).toBe(101)
  })
  it('세번째 케이스', () => {
    expect(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])).toBe(
      110
    )
  })
})
