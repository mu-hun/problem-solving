export default function substringCount(S: string, K: number) {
  const aCharCode = 'a'.charCodeAt(0)

  let count = 0

  const MAX_CHAR =
    max(S.split('').map((char) => char.charCodeAt(0) - aCharCode)) + 1

  for (const start in S.split('')) {
    const stringCount = [...new Array(MAX_CHAR)].map(() => 0)
    for (const substrig of S.split('').slice(parseInt(start))) {
      const index = substrig.charCodeAt(0) - aCharCode
      stringCount[index] += 1
      if (stringCount[index] > K) break
      if (stringCount[index] === K && check(stringCount, K) === true) count += 1
    }
  }
  return count
}

export const max = (numbers: number[]) =>
  numbers.reduce((a, b) => (a >= b ? a : b))

export function check(stringCount: number[], K: number) {
  for (const charCount of stringCount) {
    if (charCount && charCount !== K) return false
  }
  return true
}
