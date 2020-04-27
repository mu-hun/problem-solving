export default function solution(progresses: number[], speeds: number[]) {
  const answer: number[] = []

  while (progresses.length > 0) {
    progresses = progresses.map((progress, index) => progress + speeds[index])

    let count = 0
    while (progresses[0] >= 100) {
      count += 1
      progresses.shift()
      speeds.shift()
    }
    if (count > 0) answer.push(count)
  }
  return answer
}
