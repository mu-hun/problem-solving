from datetime import date

weeks = ['Monday', 'Tuesday', 'Wednesday',
         'Thursday', 'Friday', 'Saturday', 'Sunday']


def solution(M: int, D: int):
    return weeks[date(2009, M, D).weekday()]


def test_solution():
    assert solution(1, 1) == weeks[3]


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
