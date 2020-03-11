type ReducedItem = { index: number; play: number }

type Reduced = Record<string, ReducedItem[]>

export const reducer = (genres: string[], plays: number[]) =>
  genres.reduce((pre, curr, index) => {
    const append = { index, play: plays[index] }
    pre[curr] ? pre[curr].push(append) : (pre[curr] = [append])
    return pre
  }, {} as Reduced)

const sortByPlay = (items: ReducedItem[]) =>
  items.sort((a, b) => a.play - b.play).reverse()

const reducerSort = (items: Reduced) =>
  Object.entries(items).reduce((pre, curr) => {
    pre[curr[0]] = sortByPlay(curr[1])
    return pre
  }, {} as Reduced)

const accReducer = (items: Reduced) =>
  Object.keys(items).reduce((pre, curr) => {
    pre[curr] = acc(items[curr])
    return pre
  }, {} as Record<string, number>)

const acc = (reduced: ReducedItem[]) => reduced.reduce((a, b) => a + b.play, 0)

export default function solution(genres: string[], plays: number[]) {
  const reduced = reducer(genres, plays)
  const sorted = reducerSort(reduced)

  const accmulated = accReducer(sorted)
  const sortedKeys = Object.keys(accmulated).sort(
    (a, b) => accmulated[b] - accmulated[a]
  )

  return sortedKeys
    .map(key => sorted[key].slice(0, 2).map(v => v.index))
    .reduce((acc, val) => acc.concat(val), [] as number[])
}
