export const solution = (clothes: [string, string][]) =>
  Object.values(
    clothes.reduce((h, v) => {
      h[v[1]] = h[v[1]] ? h[v[1]] + 1 : 1
      return h
    }, {} as Record<string, number>)
  ).reduce((a, b) => (a *= b + 1), 1) - 1
