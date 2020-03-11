import solution, { reducer } from './42579'

describe('베스트앨범', () => {
  test('one', () => {
    expect(
      solution(
        ['classic', 'pop', 'classic', 'classic', 'pop'],
        [500, 600, 150, 800, 2500]
      )
    ).toStrictEqual([4, 1, 3, 0])
  })
})

describe('sub methods', () => {
  test('reducer', () => {
    expect(
      reducer(
        ['classic', 'pop', 'classic', 'classic', 'pop'],
        [500, 600, 150, 800, 2500]
      )
    ).toStrictEqual({
      classic: [
        { play: 500, index: 0 },
        { play: 150, index: 2 },
        { play: 800, index: 3 }
      ],
      pop: [
        { play: 600, index: 1 },
        { play: 2500, index: 4 }
      ]
    })
  })
})
