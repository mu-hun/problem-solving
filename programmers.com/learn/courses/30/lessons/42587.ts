export default function solution(priorities: number[], location: number) {
  const indexed = priorities.map((prioritie, index) => [prioritie, index])

  let count = 0

  while (indexed.length > 0) {
    const poped = indexed[0]
    indexed.splice(0, 1)

    if (indexed.length === 0) return count + 1

    const max = indexed.reduce((one, two) => (one[0] >= two[0] ? one : two))

    if (poped[0] < max[0]) {
      indexed.push(poped)
      continue
    }

    count += 1
    if (poped[1] === location) return count
  }
}
