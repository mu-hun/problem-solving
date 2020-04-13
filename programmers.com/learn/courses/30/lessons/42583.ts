export default function solution(
  bridgeLenght: number,
  weight: number,
  truckWeights: number[]
) {
  let answer = 0
  let totalTruckWeight = 0
  const bridgeQueue: number[] = [],
    weightQueue: number[] = []

  do {
    for (const i in bridgeQueue) bridgeQueue[i]--
    if (bridgeQueue[0] === 0 && weightQueue) {
      // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
      totalTruckWeight -= weightQueue.shift()!
      bridgeQueue.shift()
    }

    if (totalTruckWeight + truckWeights[0] <= weight) {
      weightQueue.push(truckWeights[0])
      bridgeQueue.push(bridgeLenght)
      // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
      totalTruckWeight += truckWeights.shift()!
    }
    answer++
  } while (bridgeQueue.length > 0)
  return answer
}
