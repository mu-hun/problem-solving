from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def go(maze: list):
    n_lenght = len(maze) - 1
    m_lenght = len(maze[0]) - 1

    mark = [[False]*(m_lenght+1) for _ in range(n_lenght+1)]
    dist = [[0]*(m_lenght+1) for _ in range(n_lenght+1)]

    q = deque()
    q.append((0, 0))
    dist[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx <= n_lenght and 0 <= ny <= m_lenght:
                if mark[nx][ny] == False and maze[nx][ny] == 1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    mark[nx][ny] = True
    return dist[n_lenght][m_lenght]


def test_go():
    maze = [[1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1]]
    assert go(maze) == 15

    maze = [[1, 1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1]]
    assert go(maze) == 9

    maze = [[1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]]
    assert go(maze) == 38

    maze = [[1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]]
    assert go(maze) == 13


if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [list(map(int, list(input()))) for _ in range(n)]

    print(go(maze))
