export function solution(skill: string, skill_trees: string[]) {
  const regex = new RegExp(`[^${skill}]`, "g")
  return skill_trees
    .map(x => x.replace(regex, ""))
    .filter(x => skill.indexOf(x) === 0 || x === "").length
}
