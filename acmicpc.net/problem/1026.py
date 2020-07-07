from typing import List, Tuple


def solution(first: List[int], second: List[int]):
    first.sort()
    second.sort(reverse=True)

    result = 0

    for index in range(len(first)):
        result += first[index] * second[index]

    return result


def test_solution():
    assert solution([1, 1, 1, 6, 0], [2, 7, 8, 3, 1]) == 18


if __name__ == "__main__":
    input()
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    print(solution(first, second))
