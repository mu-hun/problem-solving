def printSnail(N):
    x, y = 0, 0
    lastCol, lastRow = N - 1, N - 1

    snail = [i for i in range(1, N*N+1)]

    result = [[0 for i in range(N)] for i in range(N)]

    while x <= lastCol and y <= lastRow:
        for i in range(y, lastRow+1):
            result[i][x] = snail.pop()
        x += 1

        for i in range(x, lastCol+1):
            result[lastRow][i] = snail.pop()
        lastRow -= 1

        if x <= lastCol:
            for i in range(lastRow, y-1, -1):
                result[i][lastCol] = snail.pop()
            lastCol -= 1

        if y <= lastRow:
            for i in range(lastCol, x-1, -1):
                result[y][i] = snail.pop()
            y += 1
    return result


if __name__ == '__main__':
    L = printSnail(int(input()))
    S = int(input())
    for i, v in enumerate(L):
        if v.count(S):
            C = f'{i+1} {v.index(S)+1}'
        print(' '.join(map(str, v)))
    print(C)
