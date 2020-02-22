export const solution = (heights: number[]) => {
  let result: number[] = []
  const hl = heights.length
  for (let i = hl - 1; i >= 0; i--) {
    for (let j = 1; j <= i; j++) {
      if (heights[i] >= heights[i - j]) continue
      result.push(i - j + 1)
      break
    }
    if (result.length !== hl - i) result.push(0)
  }
  return result.reverse()
}
