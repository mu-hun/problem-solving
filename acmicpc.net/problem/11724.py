from typing import List


def solution(graph: List[List[int]]):
    length = len(graph)
    check = [False] * length

    def dfs(x):
        check[x] = True
        for y in graph[x]:
            if not check[y]:
                dfs(y)

    count = 0

    for x in range(length):
        if not check[x]:
            count += 1
            dfs(x)
    return count


def main():
    N, M = map(int, input().split())
    graph = [[] for __ in range(N)]

    for __ in range(M):
        A, B = map(int, input().split())
        graph[A-1].append(B-1)
        graph[B-1].append(A-1)

    return solution(graph)


def test_main():
    import io
    import sys

    sys.stdin = io.StringIO("""6 5
1 2
2 5
5 1
3 4
4 6
""")
    assert main() == 2

    sys.stdin = io.StringIO("""6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
""")
    assert main() == 1


if __name__ == '__main__':
    print(main())
