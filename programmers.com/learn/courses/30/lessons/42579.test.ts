import solution from './42579'

describe('베스트앨범', () => {
  test('one', () => {
    expect(
      solution(
        ['classic', 'pop', 'classic', 'classic', 'pop'],
        [500, 600, 150, 800, 2500]
      )
    ).toStrictEqual([4, 1, 3, 0])
  })
  test('가장 많이 재생된 장르', () => {
    expect(
      solution(
        ['classic', 'pop', 'classic', 'classic', 'pop'],
        [500, 600, 501, 800, 900]
      )
    ).toStrictEqual([3, 2, 4, 1])
  })
})
