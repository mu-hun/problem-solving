export default function countingValleys(_: number, valleys: string) {
  let count = 0
  let answer = 0
  for (const valley of valleys.split('')) {
    const UP = valley === 'U'
    count += UP ? 1 : -1
    if (count === 0 && UP) answer += 1
  }
  return answer
}
