from typing import List


def solution(graph: List[List[int]]):
    length = len(graph)
    check = [False] * length

    count = [0]

    def dfs(x=0):
        check[x] = True
        for y in graph[x]:
            if not check[y]:
                count[0] += 1
                dfs(y)

    dfs()

    return count[0]


def main():
    N = int(input())
    M = int(input())
    graph = [[] for __ in range(N)]

    for __ in range(M):
        A, B = map(int, input().split())
        graph[A-1].append(B-1)
        graph[B-1].append(A-1)

    return solution(graph)


def test_main():
    import io
    import sys

    sys.stdin = io.StringIO("""7
6
1 2
2 3
1 5
5 2
5 6
4 7
""")
    assert main() == 4


if __name__ == '__main__':
    print(main())
