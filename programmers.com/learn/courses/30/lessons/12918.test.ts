import { solution } from './12918'

describe('문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인하기', () => {
  describe('문자열의 길이가 4', () => {
    it(`알파벳이 포함된 문자열`, () => {
      expect(solution('a234')).toBe(false)
    })
    it(`숫자 문자열`, () => {
      expect(solution('1234')).toBe(true)
    })
  })
  describe('문자열의 길이가 5', () => {
    it(`알파벳이 포함된 문자열`, () => {
      expect(solution('a2345')).toBe(false)
    })
    it(`숫자 문자열`, () => {
      expect(solution('12345')).toBe(false)
    })
  })
})
describe('문자열의 길이가 6', () => {
  it(`알파벳이 포함된 문자열`, () => {
    expect(solution('2a3456')).toBe(false)
  })
  it(`숫자 문자열`, () => {
    expect(solution('123456')).toBe(true)
  })
})
