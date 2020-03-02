const total = (bridgeCase: number[]) =>
  bridgeCase.length === 0 || bridgeCase.reduce((a, b) => a + b)

export default function solution(
  bridge_lenght: number,
  weight: number,
  truck_weights: number[]
) {
  let timer = 0
  let step = 0
  let bridgeQueue: number[] = [],
    weightQueue: number[] = []

  do {} while (bridgeQueue.length > 0)

  return timer
}
