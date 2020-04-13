const [method, uid, name] = [0, 1, 2] as const

const uid2Name: Record<string, string> = {}

const isEdit = {
  Enter: true,
  Change: true,
  Leave: false,
} as const

type message = ['Enter' | 'Change' | 'Leave', string, string]

const inOrOut = {
  Enter: '들어왔습니다',
  Leave: '나갔습니다',
  Change: null,
} as const

export function solution(record: string[]) {
  const answer: string[] = []

  for (const message of record) {
    const splited = message.split(' ') as message

    if (isEdit[splited[method]]) uid2Name[splited[uid]] = splited[name]
  }

  for (const message of record) {
    const splited = message.split(' ') as message

    if (splited[method] === 'Change') continue

    answer.push(`${uid2Name[splited[uid]]}님이 ${inOrOut[splited[method]]}.`)
  }

  return answer
}
