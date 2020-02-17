import { solution } from './42748'

test('case', () => {
  expect(
    solution(
      [1, 5, 2, 6, 3, 7, 4],
      [
        [2, 5, 3],
        [4, 4, 1],
        [1, 7, 3]
      ]
    )
  ).toStrictEqual([5, 6, 3])
})
