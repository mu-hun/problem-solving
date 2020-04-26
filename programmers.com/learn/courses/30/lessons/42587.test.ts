import solution from './42587'

describe('프린터 큐 [2, 1, 3, 2] 중에서', () => {
  test('2번째 큐가 1번째로 인쇄된다', () => {
    expect(solution([2, 1, 3, 2], 2)).toBe(1)
  })
})

describe('프린터 큐 [1, 1, 9, 1, 1, 1] 중에서', () => {
  test('0번째 큐가 5번째로 인쇄된다', () => {
    expect(solution([1, 1, 9, 1, 1, 1], 0)).toBe(5)
  })
})

describe('프린터 큐 [1,2,3] 중에서', () => {
  test('0번째 큐가 3번째로 인쇄된다', () => {
    expect(solution([1, 2, 3], 0)).toBe(3)
  })
})
