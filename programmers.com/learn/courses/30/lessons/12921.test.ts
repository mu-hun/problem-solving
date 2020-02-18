import { solution } from './12921'

describe('소수 찾기', () => {
  it('1부터 10까지 소수의 갯수', () => {
    expect(solution(10)).toBe(4)
  })
  it('1부터 5까지 소수의 갯수', () => {
    expect(solution(5)).toBe(3)
  })
})
