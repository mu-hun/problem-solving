memo = [[[0 for __ in range(21)] for __ in range(21)] for __ in range(21)]


def isMemo(a, b, c):
    return (0 <= a and a <= 20) and (0 <= b and b <= 20) and (0 <= c and c <= 20)


def w(a, b, c):
    if isMemo(a, b, c) and memo[a][b][c] > 0:
        return memo[a][b][c]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        memo[20][20][20] = w(20, 20, 20)
        return memo[20][20][20]

    if a < b and b < c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]

    memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
        w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memo[a][b][c]


def test_w():
    assert w(1, 1, 1) == 2
    assert w(2, 2, 2) == 4
    assert w(10, 4, 6) == 523
    assert w(50, 50, 50) == 1048576
    assert w(-1, 7, 18) == 1


if __name__ == '__main__':
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == -1:
            break
        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
