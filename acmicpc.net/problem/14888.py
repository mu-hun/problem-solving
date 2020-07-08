from typing import List, Tuple


def solution(A: List[int], operators: Tuple[int, int, int, int]):
    def calc(A: List[int], index: int, current: int, plus: int, minus: int, mul: int, div: int):
        if index == len(A):
            return (current, current)
        result = []
        if plus > 0:
            result.append(
                calc(A, index+1, current+A[index], plus-1, minus, mul, div))
        if minus > 0:
            result.append(calc(A, index+1, current -
                               A[index], plus, minus-1, mul, div))
        if mul > 0:
            result.append(calc(A, index+1, current *
                               A[index], plus, minus, mul-1, div))
        if div > 0:
            if current >= 0:
                result.append(calc(A, index+1, current //
                                   A[index], plus, minus, mul, div-1))
            else:
                result.append(calc(A, index+1, -(-current //
                                                 A[index]), plus, minus, mul, div-1))
        return (max([item[0] for item in result]), min([item[1] for item in result]))
    return calc(A, 1, A[0], *operators)


def test_calc():
    one = [5, 6]
    assert solution(one, (0, 0, 1, 0)) == (30, 30)

    two = [3, 4, 5]
    assert solution(two, (1, 0, 1, 0)) == (35, 17)

    three = [1, 2, 3, 4, 5, 6]
    assert solution(three, (2, 1, 1, 1)) == (54, -24)


if __name__ == '__main__':
    input()
    A = list(map(int, input().split()))

    ans = solution(A, tuple(map(int, input().split())))
    print(ans[0])
    print(ans[1])
