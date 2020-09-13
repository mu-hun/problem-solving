from typing import Tuple


def main(goal: int, brokens: Tuple[bool]):
    def pressButton(subGoal: int):
        if subGoal == 0:
            if brokens[0]:
                return 0
            return 1
        count = 0
        while subGoal > 0:
            if brokens[subGoal % 10]:
                return 0
            count += 1
            subGoal //= 10
        return count

    answer = abs(goal - 100)
    for subGoal in range(0, 1000001):
        first_step = pressButton(subGoal)
        if first_step == 0:
            continue
        second_step = abs(subGoal - goal)
        if answer > first_step + second_step:
            answer = first_step + second_step
    return answer


def test_main():
    assert main(5457, (False, False, False, False,
                       False, False, True, True, True, False)) == 6


if __name__ == "__main__":
    goal = int(input())
    count = int(input())
    brokens = [False] * 10
    if count > 0:
        for index in map(int, input().split()):
            brokens[index] = True
    print(main(goal, tuple(brokens)))
