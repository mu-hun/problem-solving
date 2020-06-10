from typing import List


def solution(array: List[int]):
    current_max = 0
    maximum = -1000

    for item in array:
        current_max += item
        maximum = max(maximum, current_max)
        if current_max < 0:
            current_max = 0
    return maximum


def test_solution():
    assert solution([1, 2, 3, 4, 5]) == 15
    assert solution([2, 1, -2, 3, -5]) == 4


if __name__ == "__main__":
    for __ in range(int(input())):
        input()
        print(solution(list(map(int, input().split()))))
