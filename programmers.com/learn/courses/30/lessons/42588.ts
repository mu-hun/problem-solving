export const solution = (heights: number[]) =>
  heights.map((v, i) => {
    while (i >= 0) {
      --i
      if (v < heights[i]) return i + 1
    }
    return 0
  })
