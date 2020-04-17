export default function countingValleys(_: number, valleys: string) {
  const lineGraph = createLineGraph(valleys.split(''))
  const answer = lineGraph.reduce(
    (count, valley, index) =>
      count + (valley === 0 && lineGraph[index - 1] === -1 ? 1 : 0),
    0
  )
  return answer
}

export const createLineGraph = (valleys: string[]) =>
  valleys
    .reduce(
      (passed, next) => {
        const nextValue = next === 'U' ? 1 : -1
        return [...passed, passed[passed.length - 1] + nextValue]
      },
      [0]
    )
    .slice(1)
