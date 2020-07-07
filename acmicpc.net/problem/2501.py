from math import sqrt, floor


def solution(N: int, K: int):
    measures = []
    for divTo in range(1, floor(sqrt(N))+1):
        if N % divTo == 0:
            measures.append(N // divTo)
            if divTo * divTo != N:
                measures.append(divTo)
    if len(measures) < K:
        return 0
    measures.sort()
    return measures[K-1]


def test_solution():
    assert solution(6, 3) == 3
    assert solution(6, 10) == 0


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
