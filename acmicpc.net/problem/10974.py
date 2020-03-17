def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return a


if __name__ == "__main__":
    IN = [i + 1 for i in range(int(input()))]

    print(*IN)
    for i in IN:
        next_permutated = next_permutation(IN)
        while next_permutated:
            print(*next_permutated)
            next_permutated = next_permutation(IN)
