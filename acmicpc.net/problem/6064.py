def year_count(M: int, N: int, X: int, Y: int):
    X -= 1
    Y -= 1

    K = X
    while K < M * N:
        if K % N == Y:
            return K + 1
        K += M
    return -1


def test_year_count():
    assert year_count(10, 12, 3, 9) == 33
    assert year_count(10, 12, 7, 2) == -1
    assert year_count(13, 11, 5, 6) == 83


if __name__ == "__main__":
    for __ in range(int(input())):
        print(year_count(*map(int, input().split())))
