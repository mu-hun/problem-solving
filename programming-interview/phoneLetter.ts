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
  const s = new Array<number>(n).fill(0)
  const result: number[][] = []

  // eslint-disable-next-line no-constant-condition
  while (true) {
    result.push([...s])

    for (let i = n - 1; i >= -1; i--) {
      if (i === -1) return result
      if (s[i] === k - 1) {
        s[i] = 0
        continue
      }
      s[i] += 1
      break
    }
  }
}
