def go(sum: int, goal: int):
    if sum > goal:
        return 0
    if sum == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(sum+i, goal)
    return now


def test_go():
    assert go(0, 4) == 7
    assert go(0, 7) == 44
    assert go(0, 10) == 274


def main():
    num = int(input())
    for _ in range(num):
        goal = int(input())
        print(go(0, goal))


if __name__ == '__main__':
    main()
