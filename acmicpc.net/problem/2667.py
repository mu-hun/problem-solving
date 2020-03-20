from collections import deque, Counter
from functools import reduce

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

A = []
M = []
N = 0


def insert_map():
    global M, N, A
    N = int(input())
    M = [list(map(int, list(input()))) for _ in range(N)]
    A = [[0]*N for _ in range(N)]


def main():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if M[i][j] == 1 and A[i][j] == 0:
                cnt += 1
                bfs(i, j, cnt)


def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    A[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            ax, ay = x+dx[i], y+dy[i]
            if 0 <= ax < N and 0 <= ay < N and M[ax][ay] == 1 and A[ax][ay] == 0:
                A[ax][ay] = cnt
                q.append((ax, ay))


if __name__ == '__main__':
    insert_map()
    main()
    ans = list(reduce(lambda x, y: x+y, A))
    ans = [x for x in ans if x > 0]
    cnt = sorted(list(Counter(ans).values()))
    print(len(cnt))
    print('\n'.join(map(str, cnt)))
