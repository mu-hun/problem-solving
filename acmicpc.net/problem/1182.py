if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    def go(i, s):
        global ans
        if i == n:
            if s == m:
                ans += 1
            return
        go(i+1, s+a[i])
        go(i+1, s)

    go(0, 0)
    if m == 0:
        ans -= 1
    print(ans)
