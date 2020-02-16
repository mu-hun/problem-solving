const sort = (a: number, b: number) => a - b

const difference = (setA: Set<number>, setB: Set<number>) => {
  let _difference = new Set(setA)
  for (const item of setB) {
    _difference.delete(item)
  }
  return _difference
}

const getDifference = (_a: number[], _b: number[]) => {
  const setA = new Set(_a.sort(sort))
  const setB = new Set(_b.sort(sort))

  return [[...difference(setA, setB)], [...difference(setB, setA)]]
}

export function solution(n: number, _lost: number[], _reserve: number[]) {
  let registerable = [...new Array(n + 1).keys()].slice(1)
  const [lost, reserve] = getDifference(_lost, _reserve)

  for (const lostPerson of lost) {
    if (
      !reserve.includes(lostPerson - 1) &&
      !reserve.includes(lostPerson + 1)
    ) {
      registerable.splice(lostPerson - 1, 1)
      continue
    }

    if (reserve.includes(lostPerson + 1) && !reserve.includes(lostPerson - 1)) {
      const target = lostPerson + 1
      const index = reserve.findIndex(v => v === target)

      reserve.splice(index, 1)
      continue
    }
    if (reserve.includes(lostPerson - 1) && !reserve.includes(lostPerson + 1)) {
      const target = lostPerson - 1
      const index = reserve.findIndex(v => v === target)

      reserve.splice(index, 1)
      continue
    }
  }

  return registerable.length
}
