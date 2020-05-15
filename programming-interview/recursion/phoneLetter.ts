const numpad = [
  ['0', '0', '0'],
  ['1', '1', '1'],
  ['A', 'B', 'C'],
  ['D', 'E', 'F'],
  ['G', 'H', 'I'],
  ['J', 'K', 'L'],
  ['M', 'N', 'O'],
  ['P', 'R', 'S'],
  ['T', 'U', 'V'],
  ['W', 'X', 'Y'],
]

export default function phoneNumberToLetter(phoneNumber: number) {
  const array = toNumberArray(phoneNumber)
  const combinations = combination(array.length, 3)

  const result = combinations.map((item) =>
    item.map((value, index) => numpad[array[index]][value]).join('')
  )

  return result
}

export function toNumberArray(number: number) {
  const splited: number[] = []

  while (number > 0) {
    splited.push(number % 10)
    number = Math.floor(number / 10)
  }

  return splited.reverse()
}

export function combination(n: number, k: number) {
  const result: number[][] = []
  function go(index: number, set: number[]) {
    if (index === n) {
      result.push(set)
      return
    }
    for (let i = 0; i < k; i++) {
      go(index + 1, [...set, i])
    }
  }

  go(0, [])

  return result
}
