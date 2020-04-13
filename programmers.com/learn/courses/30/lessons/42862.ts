const diff = (a: number[], b: number[]) => a.filter((x) => !b.includes(x))

export const solution = (n: number, lost: number[], reserve: number[]) =>
  diff(lost, reserve).reduce(
    ({ attend, spares }, index) => {
      const target = [index + 1, index - 1].find((x) => spares.includes(x))
      return target
        ? { attend, spares: spares.filter((spare) => target !== spare) }
        : { attend: attend - 1, spares }
    },
    { attend: n, spares: diff(reserve, lost) }
  ).attend
