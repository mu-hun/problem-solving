export const one = [1, 2, 3, 4, 5]
const two = [2, 1, 2, 3, 2, 4, 2, 5]
const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

export const expendArray = (expendSize: number) => (array: number[]) => {
  const toExpend = expendSize - array.length
  const arrayLength = array.length

  let result: number[] = []
  for (let i = 0; result.length < expendSize; i++) {
    if (i === arrayLength) i = 0
    result.push(array[i])
  }

  return result
}

export const matchArrayCount = (answers: number[]) => (b: number[]) =>
  answers.filter((value, index) => value === b[index]).length

const expendArrayEach = (len: number) => {
  const expendArrayOf = expendArray(len)
  return {
    one: expendArrayOf(one),
    two: expendArrayOf(two),
    three: expendArrayOf(three)
  }
}

export default function solution(answers: number[]) {
  const len = answers.length
  const { one, two, three } = expendArrayEach(len)
  const matchArrayCountOf = matchArrayCount(answers)

  const a = matchArrayCountOf(one)
  const b = matchArrayCountOf(two)
  const c = matchArrayCountOf(three)

  if (a === b && b === c) return [1, 2, 3]

  return [
    { key: 1, value: a },
    { key: 2, value: b },
    { key: 3, value: c }
  ].sort((a, b) => a.value - b.value)[0].key
}
