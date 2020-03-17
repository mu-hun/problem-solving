if __name__ == "__main__":
    N = int(input())
    L = [int(input()) for __ in range(N)]
    A = -1

    L.sort()

    for i in range(N-1, 1, -1):
        line_a = L[i]
        line_b = L[i-1]
        line_c = L[i-2]
        if (line_a < line_b+line_c):
            A = line_a+line_b+line_c
            break
    print(A)
