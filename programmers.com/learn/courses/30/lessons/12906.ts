export const solution = (arr: number[]) =>
  [...arr, 10].reduce(
    ({ value, result }, current) =>
      value !== current
        ? { value: current, result: [...result, value] }
        : { value: current, result },
    { value: arr[0], result: [] as number[] }
  ).result
