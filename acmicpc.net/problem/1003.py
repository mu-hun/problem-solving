zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(n):
    l = len(zero)
    if l <= n:
        for i in range(l, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(f'{zero[n]} {one[n]}')


for __ in range(int(input())):
    fibo(int(input()))
