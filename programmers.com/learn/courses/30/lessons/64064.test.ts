import solution, { choose } from './64064'

test('solution 1', () => {
  expect(
    solution(
      ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc'],
      ['fr*d*', 'abc1**']
    )
  ).toBe(2)
})

test('solution 2', () => {
  expect(
    solution(
      ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc'],
      ['*rodo', '*rodo', '******']
    )
  ).toBe(2)
})

test('solution 3', () => {
  expect(
    solution(
      ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc'],
      ['fr*d*', '*rodo', '******', '******']
    )
  ).toBe(3)
})

test('choose', () => {
  expect(choose(['1', '2', '3'], 2)).toEqual([
    ['1', '2'],
    ['1', '3'],
    ['2', '3']
  ])
})
