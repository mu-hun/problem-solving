const sort = (a: number, b: number) => a - b

export const solution = (
  array: number[],
  commands: [number, number, number][]
) =>
  commands.map(
    (command) =>
      array.slice(command[0] - 1, command[1]).sort(sort)[command[2] - 1]
  )
