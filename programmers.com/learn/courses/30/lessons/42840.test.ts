import solution, { expendArray, one, matchArrayCount } from './42840'

test('expendArray: 1 ~ 5', () => {
  expect(expendArray(6)(one)).toStrictEqual([1, 2, 3, 4, 5, 1])
})

test('matchArrayCount', () => {
  expect(matchArrayCount([1, 2, 3])([1, 3])).toBe(1)
})

describe('모의고사', () => {
  test('1회차', () => {
    expect(solution([1, 2, 4, 5])).toBe([1])
  })
  test('2회차', () => {
    expect(solution([1, 2, 4, 2])).toBe([1, 2, 3])
  })
})
