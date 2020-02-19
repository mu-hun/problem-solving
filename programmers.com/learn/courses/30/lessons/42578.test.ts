import { solution } from './42578'

describe('위장', () => {
  test('예제 #1', () => {
    expect(
      solution([
        ['yellow_hat', 'headgear'],
        ['blue_sunglasses', 'eyewear'],
        ['green_turban', 'headgear']
      ])
    ).toBe(5)
  })
  test('예제 #2', () => {
    expect(
      solution([
        ['crow_mask', 'face'],
        ['blue_sunglasses', 'face'],
        ['smoky_makeup', 'face']
      ])
    ).toBe(3)
  })
})
