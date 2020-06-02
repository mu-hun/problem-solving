from typing import List, Tuple


def solution(values: List[int], target: Tuple[int, int]):
    length = len(values)
    sums = [[0]*length for __ in range(length)]

    sums[0][0] = values[0][0]
    for y in range(1, length):
        sums[y][0] = sums[y-1][0] + values[y][0]

    for x in range(1, length):
        sums[0][x] = sums[0][x-1] + values[0][x]

    for y in range(1, length):
        for x in range(1, length):
            sums[y][x] = max(sums[y-1][x], sums[y][x-1]) + values[y][x]

    return sums[target[0]][target[1]]


def test_solution():
    values = [[3, 7, 9, 2, 7],
              [9, 8, 3, 5, 5],
              [1, 7, 9, 8, 5],
              [3, 8, 6, 4, 10],
              [6, 3, 9, 7, 8]]
    assert solution(values, (1, 1)) == 20
    assert solution(values, (4, 4)) == 67


if __name__ == "__main__":
    test_solution()
