dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def go(maze: list):
    n_length = len(maze)
    m_length = len(maze[0])
    n_max_index = n_length - 1
    m_max_index = m_length - 1

    mark = [[False]*m_length for _ in range(n_length)]
    dist = [[0]*m_length for _ in range(n_length)]

    queue = [(0, 0)]
    dist[0][0] = 1

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            in_range = 0 <= nx <= n_max_index and 0 <= ny <= m_max_index
            can_go_forward = in_range and mark[nx][ny] == False and maze[nx][ny] == 1

            if can_go_forward:
                queue.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                mark[nx][ny] = True

    return dist[n_max_index][m_max_index]


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
    maze = [list(map(int, input().split())) for _ in range(n)]

    print(go(maze))
