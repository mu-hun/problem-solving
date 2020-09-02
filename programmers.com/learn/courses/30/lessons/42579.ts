interface Item {
  playCount: number
  index: number
}

export default function solution(genres: string[], plays: number[]) {
  const reduced = genres.reduce((toReduce, key, index) => {
    const toPush = { playCount: plays[index], index }
    toReduce[key] ? toReduce[key].push(toPush) : (toReduce[key] = [toPush])

    return toReduce
  }, {} as Record<string, Item[]>)

  for (const key of Object.keys(reduced)) {
    reduced[key].sort((a, b) => {
      const calculated = b.playCount - a.playCount
      if (calculated === 0) return a.index - b.index
      return calculated
    })
  }

  const genreKeys = Object.keys(reduced).sort(
    (alice, bob) =>
      reduced[bob].reduce((acc, item) => acc + item.playCount, 0) -
      reduced[alice].reduce((acc, item) => acc + item.playCount, 0)
  )

  return (
    genreKeys
      .map(genre => reduced[genre].slice(0, 2).map(item => item.index))
      //@ts-ignore
      .flat() as number[]
  )
}
