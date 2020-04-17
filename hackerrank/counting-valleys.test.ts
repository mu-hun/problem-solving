import countingValleys, { createLineGraph } from './counting-valleys'

test('create Line graph', () => {
  expect(createLineGraph(['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U'])).toEqual([
    1,
    0,
    -1,
    -2,
    -1,
    -2,
    -1,
    0,
  ])
})

test('counting valleys', () => {
  expect(countingValleys(8, 'UDDDUDUU')).toBe(1)
})
