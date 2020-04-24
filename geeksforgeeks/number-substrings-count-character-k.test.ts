import substringCount, {
  max,
  check,
} from './number-substrings-count-character-k'

describe('sub string count, https://www.geeksforgeeks.org/number-substrings-count-character-k/', () => {
  test('string = aabbcc, K is 2. will be return 6', () => {
    expect(substringCount('aabbbcc', 2)).toBe(6)
  })
  test('string = aabbbc, K is 2. will be return 3', () => {
    expect(substringCount('aabccc', 2)).toBe(3)
  })
})

describe('max function', () => {
  test('[1, 2, 4, 3] return be 4', () => {
    expect(max([1, 2, 4, 3])).toBe(4)
  })
})

describe('check each char count equal to K', () => {
  test('[0, 4, 2], 4', () => {
    expect(check([0, 4, 4], 4)).toBe(true)
  })
})
