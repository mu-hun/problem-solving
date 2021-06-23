from typing import List


def resetCheck(length):
    return [False]*length


def solution(graph: List[List[int]], start: int):
    length = len(graph)
    answer = {'DFS': [], 'BFS': []}

    def DFS(x: int):
        answer['DFS'].append(x)
        check[x] = True
        for y in graph[x]:
            if not check[y]:
                DFS(y)

    check = resetCheck(length)
    DFS(start)

    def BFS(start: int):
        queue = []
        queue.append(start)

        check[start] = True

        while queue:
            x = queue.pop(0)
            answer['BFS'].append(x)

            for y in graph[x]:
                if not check[y]:
                    check[y] = True
                    queue.append(y)

    check = resetCheck(length)
    BFS(start)

    return answer


def main():
    N, M, start = map(int, input().split())
    graph = [[] for __ in range(N+1)]

    for __ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)

    for index in range(N+1):
        graph[index].sort()

    return solution(graph, start)


def test_main():
    import sys
    import io

    sys.stdin = io.StringIO("""4 5 1
1 2
1 3
1 4
2 4
3 4
""")
    assert main() == {'DFS': [1, 2, 4, 3], 'BFS': [1, 2, 3, 4]}

    sys.stdin = io.StringIO("""5 5 3
5 4
5 2
1 2
3 4
3 1
""")
    assert main() == {'DFS': [3, 1, 2, 5, 4], 'BFS': [3, 1, 4, 2, 5]}

    sys.stdin = io.StringIO("""1000 1 1000
999 1000
""")
    assert main() == {'DFS': [1000, 999], 'BFS': [1000, 999]}


def formatter(answer: List[int]):
    return ' '.join(map(str, answer))


if __name__ == '__main__':
    answer = main()

    print(formatter(answer['DFS']))
    print(formatter(answer['BFS']))
