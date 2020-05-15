import phoneNumberToLetter, { toNumberArray, combination } from './phoneLetter'

describe('make 123 phone letters', () => {
  test('return 3^3 cases', () => {
    expect(phoneNumberToLetter(123)).toEqual([
      '1AD',
      '1AE',
      '1AF',
      '1BD',
      '1BE',
      '1BF',
      '1CD',
      '1CE',
      '1CF',
      '1AD',
      '1AE',
      '1AF',
      '1BD',
      '1BE',
      '1BF',
      '1CD',
      '1CE',
      '1CF',
      '1AD',
      '1AE',
      '1AF',
      '1BD',
      '1BE',
      '1BF',
      '1CD',
      '1CE',
      '1CF',
    ])
  })
})

describe('unit tests', () => {
  test('make number array', () => {
    expect(toNumberArray(123)).toEqual([1, 2, 3])
  })
  test('make n x k combination', () => {
    expect(combination(3, 3)).toEqual([
      [0, 0, 0],
      [0, 0, 1],
      [0, 0, 2],
      [0, 1, 0],
      [0, 1, 1],
      [0, 1, 2],
      [0, 2, 0],
      [0, 2, 1],
      [0, 2, 2],
      [1, 0, 0],
      [1, 0, 1],
      [1, 0, 2],
      [1, 1, 0],
      [1, 1, 1],
      [1, 1, 2],
      [1, 2, 0],
      [1, 2, 1],
      [1, 2, 2],
      [2, 0, 0],
      [2, 0, 1],
      [2, 0, 2],
      [2, 1, 0],
      [2, 1, 1],
      [2, 1, 2],
      [2, 2, 0],
      [2, 2, 1],
      [2, 2, 2],
    ])
  })
})
