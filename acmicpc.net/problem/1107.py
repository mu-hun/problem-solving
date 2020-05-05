C_MAX = 1000000


def controller(goal: int, _broken: list):
    broken = [False]*10
    for index in _broken:
        broken[index] = True

    def possible(c: int):
        if c == 0:
            if broken[0]:
                return 0
            return 1
        length = 0
        while c > 0:
            if broken[c % 10]:
                return 0
            length += 1
            c //= 10

        return length

    answer = abs(goal - 100)

    for c in range(C_MAX+1):
        length = possible(c)
        if length == 0:
            continue
        press = abs(c - goal)
        if answer > length + press:
            answer = length + press
    return answer


def test_controller():
    assert controller(5457, [6, 7, 8]) == 6
    assert controller(100, [0, 1, 2, 3, 4]) == 0
    assert controller(500000, [0, 2, 3, 4, 6, 7, 8, 9]) == 11117


if __name__ == "__main__":
    goal = int(input())
    _ = input()
    brokens = map(int, input().split())
    print(controller(goal, brokens))
