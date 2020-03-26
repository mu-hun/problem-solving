export default function solution(
  bridge_lenght: number,
  weight: number,
  truck_weights: number[]
) {
  let answer = 0
  let total_truck_weight = 0
  let bridge_queue: number[] = [],
    weight_queue: number[] = []

  do {
    for (const i in bridge_queue) bridge_queue[i]--
    if (bridge_queue[0] === 0 && weight_queue) {
      total_truck_weight -= weight_queue.shift()!
      bridge_queue.shift()
    }

    if (total_truck_weight + truck_weights[0] <= weight) {
      weight_queue.push(truck_weights[0])
      bridge_queue.push(bridge_lenght)
      total_truck_weight += truck_weights.shift()!
    }
    answer++
  } while (bridge_queue.length > 0)
  return answer
}
