export const one = [1, 2, 3, 4, 5]
const two = [2, 1, 2, 3, 2, 4, 2, 5]
const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

export const resizeArray = (resizeTo: number) => (array: number[]) => {
  const toExpend = resizeTo - array.length
  const arrayLength = array.length

  if (toExpend <= 0) return array.slice(0, resizeTo)

  const result = [...array]
  for (let i = 0; result.length < resizeTo; i++) {
    if (i === arrayLength) i = 0
    result.push(array[i])
  }

  return result
}

export const matchArrayCount = (answers: number[]) => (b: number[]) =>
  answers.filter((value, index) => value === b[index]).length

const resizeArrayEach = (len: number) => {
  const resizeArrayOf = resizeArray(len)
  return {
    one: resizeArrayOf(one),
    two: resizeArrayOf(two),
    three: resizeArrayOf(three)
  }
}

export default function solution(answers: number[]) {
  const len = answers.length
  const { one, two, three } = resizeArrayEach(len)
  const matchArrayCountOf = matchArrayCount(answers)

  const a = matchArrayCountOf(one)
  const b = matchArrayCountOf(two)
  const c = matchArrayCountOf(three)

  if (a === b && b === c) return [1, 2, 3]

  return [
    { key: 1, value: a },
    { key: 2, value: b },
    { key: 3, value: c }
  ].sort((a, b) => b.value - a.value)[0].key
}
