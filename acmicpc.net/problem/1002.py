for __ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = (x1-x2)**2 + (y1-y2)**2

    if r1 == r2 and d == 0:
        print(-1)
        continue

    rplus = (r1+r2)**2
    rminus = (r1-r2)**2

    if (r1 != r2 and d < rminus) or d > rplus:
        print(0)
    elif d == rplus or d == rminus:
        print(1)
    elif d < rplus:
        print(2)
