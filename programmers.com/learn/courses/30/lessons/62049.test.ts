import solution, { palindrome } from './62049'

describe('종이접기', () => {
  test('first', () => {
    expect(solution(1)).toEqual([0])
  })
  test('second', () => {
    expect(solution(2)).toEqual([0, 0, 1])
  })
  test('third', () => {
    expect(solution(3)).toEqual([0, 0, 1, 0, 0, 1, 1])
  })
})

describe('palindrome', () => {
  test('zero', () => {
    expect(palindrome([0])).toEqual([0])
  })
  test('first', () => {
    expect(palindrome([0, 0])).toEqual([0, 0, 1])
  })
  test('second', () => {
    expect(palindrome([0, 0, 1, 0])).toEqual([0, 0, 1, 0, 0, 1, 1])
  })
})
