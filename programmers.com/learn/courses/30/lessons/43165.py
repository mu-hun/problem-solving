def solution(numbers: list, target: int):
    end = len(numbers)

    def go(index: int, acc: int):
        if index == end:
            if acc == target:
                return 1
            return 0
        return go(index+1, acc-numbers[index]) + go(index+1, acc+numbers[index])

    return go(0, 0)


def test_solution():
    assert solution([1, 1, 1, 1, 1], 3) == 5
