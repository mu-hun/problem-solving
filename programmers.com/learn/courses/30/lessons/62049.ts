export default function solution(n: number) {
  let result: number[] = []
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  for (const _ in [...new Array(n)]) {
    result.push(0)
    result = palindrome(result)
  }
  return result
}

export function palindrome(list: number[]) {
  if (list.length === 1) return list
  for (let i = list.length - 2; i >= 0; i--) {
    list.push(list[i] === 1 ? 0 : 1)
  }
  return list
}
