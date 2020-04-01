export default function solution(user_id: string[], banned_id: string[]) {
  const chooseds = choose(user_id, banned_id.length)

  const banned_id_regexp = banned_id.map(
    id => new RegExp('^' + id.replace(/\*/g, '([a-z0-9])') + '$')
  )
  function isVaild(set: string[]) {
    let store = [...new Array(banned_id.length)].map(() => false)
    for (const regexpIndex in banned_id_regexp) {
      for (const setIndex in set) {
        if (banned_id_regexp[regexpIndex].test(set[setIndex]))
          store[regexpIndex] = true
      }
    }
    return !store.includes(false)
  }

  return chooseds.filter(choosed => isVaild(choosed)).length
}

export function choose(user_id: string[], num: number) {
  let result: string[][] = []
  function go(selects: string[], index: number) {
    if (index === user_id.length) {
      if (selects.length === num) result.push(selects)
      return
    }
    go([...selects, user_id[index]], index + 1)
    go(selects, index + 1)
  }
  go([], 0)
  return result
}
