export function solution(skill: string, skillTrees: string[]) {
  const regex = new RegExp(`[^${skill}]`, 'g')
  return skillTrees
    .map((x) => x.replace(regex, ''))
    .filter((x) => skill.indexOf(x) === 0 || x === '').length
}
