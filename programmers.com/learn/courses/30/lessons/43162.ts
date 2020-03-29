export default function solution(n: number, computers: number[][]) {
  let check = [...Array(n)].map(() => false)
  function dfs(x: number) {
    check[x] = true
    for (let y = 0; y < n; y++)
      if (check[y] === false && computers[x][y]) dfs(y)
  }

  let ans = 0

  for (let i = 0; i < n; i++) {
    if (check[i] === false) {
      dfs(i)
      ans += 1
    }
  }
  return ans
}
