def go(n: int):
    d = [None]*(n+1)
    d[1] = 0
    for i in range(2, n+1):
        d[i] = d[i-1] + 1
        if i % 2 == 0 and d[i] > d[i//2] + 1:
            d[i] = d[i//2] + 1
        if i % 3 == 0 and d[i] > d[i//3] + 1:
            d[i] = d[i//3] + 1
    return d[n]


def test_go():
    assert go(2) == 1
    assert go(10) == 3


if __name__ == "__main__":
    print(go(int(input())))
