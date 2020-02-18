export const solution = (n: number) => {
  let count = 0
  const check = Array(n + 1)

  for (let i = 2; i <= n; i++) {
    if (check[i]) continue
    count += 1
    for (let j = i * i; j <= n; j += i) check[j] = true
  }
  return count
}
