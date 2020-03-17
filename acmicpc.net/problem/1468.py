import sys
sys.setrecursionlimit(10000000)


def top(n: int, d: list):
    if n == 1:
        return 0
    if d[n]:
        return d[n]
    d[n] = top(n-1, d) + 1
    if (n % 2 == 0):
        temp = top(n//2, d) + 1
        if d[n] > temp:
            d[n] = temp

    if (n % 3 == 0):
        temp = top(n//3, d) + 1
        if d[n] > temp:
            d[n] = temp

    return d[n]


def test_top():
    assert top(2, [None]*3) == 1
    assert top(10, [None]*11) == 3


if __name__ == "__main__":
    n = int(input())
    print(top(n, [None]*n))
