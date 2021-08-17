from typing import List


def check(paper: str, mid: int):
    for index in range(mid):
        if paper[index] == paper[mid * 2 - index]:
            return False

    return True


def check_opposite(paper: str):
    if len(paper) == 1:
        return True

    mid = len(paper) // 2

    return check(paper, mid) and check_opposite(paper[:mid]) and check_opposite(paper[mid+1:])


def test_solution():
    assert check_opposite([0]) == True
    assert check_opposite([0, 0, 0]) == False
    assert check_opposite([0, 0, 1]) == True
    assert check_opposite([0, 0, 1, 0, 0, 1, 1]) == True


if __name__ == '__main__':
    for __ in range(int(input())):
        if check_opposite(input()):
            print('YES')
        else:
            print('NO')
