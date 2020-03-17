def turret(x1, y1, r1, x2, y2, r2):
    d = (x1-x2)**2 + (y1-y2)**2

    if r1 == r2 and d == 0:
        return -1

    rplus = (r1+r2)**2
    rminus = (r1-r2)**2

    if (r1 != r2 and d < rminus) or d > rplus:
        return 0
    elif d == rplus or d == rminus:
        return 1
    elif d < rplus:
        return 2


def test_turret():
    assert turret(0, 0, 13, 40, 0, 37) == 2
    assert turret(0, 0, 3, 0, 7, 4) == 1
    assert turret(1, 1, 1, 1, 1, 5) == 0


if __name__ == "__main__":
    for __ in range(int(input())):
        print(turret(*map(int, input().split())))
