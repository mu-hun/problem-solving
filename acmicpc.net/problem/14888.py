def calc(a, index, cur, plus, minus, mul, div):
    if index == len(a):
        return (cur, cur)
    res = []
    if plus > 0:
        res.append(calc(a, index+1, cur+a[index], plus-1, minus, mul, div))
    if minus > 0:
        res.append(calc(a, index+1, cur-a[index], plus, minus-1, mul, div))
    if mul > 0:
        res.append(calc(a, index+1, cur*a[index], plus, minus, mul-1, div))
    if div > 0:
        if cur >= 0:
            res.append(
                calc(a, index+1, cur//a[index], plus, minus, mul, div-1))
        else:
            res.append(
                calc(a, index+1, -(-cur//a[index]), plus, minus, mul, div-1))
    ans = (
        max([t[0] for t in res]),
        min([t[1] for t in res])
    )

    return ans


def test_calc():
    one = [5, 6]
    assert calc(one, 1, one[0], 0, 0, 1, 0) == (30, 30)

    two = [3, 4, 5]
    assert calc(two, 1, two[0], 1, 0, 1, 0) == (35, 17)

    three = [1, 2, 3, 4, 5, 6]
    assert calc(three, 1, three[0], 2, 1, 1, 1) == (54, -24)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    plus, minus, mul, div = map(int, input().split())

    ans = calc(A, 1, A[0], plus, minus, mul, div)
    print(ans[0])
    print(ans[1])
