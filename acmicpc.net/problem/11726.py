def solution(n):
    d = [None]*(n+1)
    d[0] = 1
    d[1] = 1

    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
        d[i] %= 10007

    return d[n]


def test_solution():
    assert solution(2) == 2
    assert solution(9) == 55


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
