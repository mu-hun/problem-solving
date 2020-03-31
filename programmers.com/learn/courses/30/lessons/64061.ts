export default function solution(board: number[][], moves: number[]) {
  const stack = new Stack()

  for (const move of moves) {
    for (const height in board) {
      if (board[height][move - 1] !== 0) {
        stack.append(board[height][move - 1])
        board[height][move - 1] = 0
        break
      }
    }
  }

  return stack.popped
}

class Stack {
  list: number[]
  popped: number
  constructor() {
    this.list = []
    this.popped = 0
  }
  append(item: number) {
    if (this.list.length && this.list[this.list.length - 1] === item) {
      this.list.pop()
      this.popped += 2
      return
    }
    this.list.push(item)
  }
}
