zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(n):
    l = len(zero)
    if l <= n:
        for i in range(l, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    return f'{zero[n]} {one[n]}'


def test_fibo():
    assert fibo(0) == '1 0'
    assert fibo(1) == '0 1'
    assert fibo(3) == '1 2'


if __name__ == '__main__':
    for __ in range(int(input())):
        print(fibo(int(input())))
