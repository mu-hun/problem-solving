import solution, { searchSegments, SearchSegments } from './12979'

const cases: SearchSegments[] = [
  { total: 11, stations: [3, 10], radius: 1 },
  { total: 16, stations: [8], radius: 2 }
]

describe('기지국 설치', () => {
  it(cases[0].toString(), () => {
    const { total, stations, radius } = cases[0]
    expect(solution(total, stations, radius)).toBe(3)
  })
  it(cases[1].toString(), () => {
    const { total, stations, radius } = cases[1]
    expect(solution(total, stations, radius)).toBe(3)
  })
})

describe('단절된 구간 찾기', () => {
  it(cases[0].toString(), () => {
    expect(searchSegments(cases[0])).toStrictEqual([
      [0, 1],
      [5, 8]
    ])
  })
  it(cases[1].toString(), () => {
    expect(searchSegments(cases[1])).toStrictEqual([
      [0, 5],
      [11, 15]
    ])
  })
})
