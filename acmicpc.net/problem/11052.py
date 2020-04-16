def buy_card(n: int, p: list):
    d = [0]*(n+1)

    for i in range(1, n+1):
        for j in range(1, i+1):
            d[i] = max(d[i], d[i-j] + p[j-1])

    return d[n]


def test_buy_card():
    assert buy_card(4, [1, 5, 6, 7]) == 10
    assert buy_card(5, [10, 9, 8, 7, 6]) == 50
    assert buy_card(10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 55
    assert buy_card(10, [5, 10, 11, 12, 13, 30, 35, 40, 45, 47]) == 50
    assert buy_card(4, [5, 2, 8, 10]) == 20
    assert buy_card(4, [3, 5, 15, 16]) == 18


if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split(' ')))
    print(buy_card(n, p))
