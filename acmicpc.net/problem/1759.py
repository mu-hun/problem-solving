def check(password: str):
    ja = 0
    mo = 0
    for char in password:
        if char in ['a', 'e', 'i', 'o', 'u']:
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def go(n: int, alpha: list, password: str, i: int):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    go(n, alpha, password + alpha[i], i+1)
    go(n, alpha, password, i+1)


if __name__ == '__main__':
    L, C = map(int, input().split())
    alpha = input().split()
    alpha.sort()
    go(L, alpha, '', 0)
