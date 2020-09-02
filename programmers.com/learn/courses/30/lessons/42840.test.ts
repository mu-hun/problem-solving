import solution, { resizeArray, one, matchArrayCount } from './42840'

test('resizeArray: 1 ~ 5', () => {
  expect(resizeArray(6)(one)).toStrictEqual([1, 2, 3, 4, 5, 1])
})

test('matchArrayCount', () => {
  expect(matchArrayCount([1, 2, 3, 4, 5])(one)).toBe(5)
})

describe('모의고사', () => {
  test('1회차', () => {
    expect(solution([1, 2, 3, 4, 5])).toBe(1)
  })
  test('2회차', () => {
    expect(solution([1, 3, 2, 4, 2])).toEqual([1, 2, 3])
  })
})
