export default function solution(
  total: number,
  _stations: number[],
  radius: number
) {
  const stations = _stations.map(station => station - 1)
  const segments = searchSegments({ total, stations, radius })

  const bandwidth = radius * 2 + 1
  let answer = 0

  for (const segment of segments) {
    const [start, end] = segment
    const range = end - start + 1
    answer += Math.ceil(range / bandwidth)
  }
  return answer
}

export interface SearchSegments {
  total: number
  stations: number[]
  radius: number
}

export function searchSegments({ total, stations, radius }: SearchSegments) {
  const startPoint = stations[0] - radius
  const endPoint = stations[stations.length - 1] + radius

  const segments: [number, number][] = []

  if (startPoint > 0) {
    segments.push([0, startPoint - 1])
  }

  for (const i of stations.keys()) {
    const start = stations[i] + radius + 1
    const end = stations[i + 1] - radius - 1
    if (start <= end) segments.push([start, end])
  }

  if (endPoint < total - 1) {
    segments.push([endPoint + 1, total - 1])
  }

  return segments
}
