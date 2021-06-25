from collections import deque


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def solution(store: list[list[int]]):
    n_length = len(store)
    m_length = len(store[0])

    distance = [[-1]*m_length for __ in range(n_length)]

    queue = deque()

    for n in range(n_length):
        for m in range(m_length):
            if store[n][m] == 1:
                distance[n][m] = 0
                queue.append((n, m))

    while queue:
        n, m = queue.popleft()
        for i in range(4):
            next_x = dx[i] + n
            next_y = dy[i] + m

            is_in_store = 0 <= next_x < n_length and 0 <= next_y < m_length

            if is_in_store and store[next_x][next_y] == 0 and distance[next_x][next_y] == -1:
                distance[next_x][next_y] = distance[n][m] + 1
                queue.append((next_x, next_y))

    answer = max([max(row) for row in distance])

    for n in range(n_length):
        for m in range(m_length):
            if store[n][m] == 0 and distance[n][m] == -1:
                answer = -1

    return answer


def main():
    N = int(input().split()[1])
    store = [list(map(int, input().split())) for __ in range(N)]
    return solution(store)


def test_main():
    import sys
    import io
    sys.stdin = io.StringIO("""6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
""")
    assert main() == 8

    sys.stdin = io.StringIO("""6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
""")
    assert main() == -1

    sys.stdin = io.StringIO("""6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
""")
    assert main() == 6

    sys.stdin = io.StringIO("""5 5
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0
""")
    assert main() == 14

    sys.stdin = io.StringIO("""2 2
1 -1
-1 1
""")
    assert main() == 0


if __name__ == '__main__':
    print(main())
