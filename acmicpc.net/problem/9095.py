def go(sum: int, goal: int):
    if sum > goal:
        return 0
    if sum == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(sum+i, goal)
    return now


def dp(n: int):
    d = [0]*(n+1)
    d[0] = 1
    for i in range(1, n+1):
        if i-1 >= 0:
            d[i] += d[i-1]
        if i-2 >= 0:
            d[i] += d[i-2]
        if i-3 >= 0:
            d[i] += d[i-3]
    return d[n]


def test_go():
    assert go(0, 4) == 7
    assert go(0, 7) == 44
    assert go(0, 10) == 274


def test_dp():
    assert dp(4) == 7
    assert dp(7) == 44
    assert dp(10) == 274


def main():
    num = int(input())
    for _ in range(num):
        goal = int(input())
        print(go(0, goal))


if __name__ == '__main__':
    main()
