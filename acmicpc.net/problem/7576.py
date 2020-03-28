from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def house(store: list):
    q = deque()

    x_lenght = len(store)
    y_lenght = len(store[0])

    dist = [[-1]*y_lenght for _ in range(x_lenght)]

    for i in range(x_lenght):
        for j in range(y_lenght):
            if store[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            ax, ay = dx[i]+x, dy[i]+y
            if 0 <= ax < x_lenght and 0 <= ay < y_lenght:
                if store[ax][ay] == 0 and dist[ax][ay] == -1:
                    dist[ax][ay] = dist[x][y] + 1
                    q.append((ax, ay))

    ans = max([max(row) for row in dist])

    for i in range(x_lenght):
        for j in range(y_lenght):
            if store[i][j] == 0 and dist[i][j] == -1:
                ans = -1
    return ans


def test_house():
    store = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1]]
    assert house(store) == 8


if __name__ == "__main__":
    M, N = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(N)]

    print(house(store))
