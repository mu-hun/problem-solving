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


def test_permutation():
    assert next_permutation([1, 2, 3, 4]) == [1, 2, 4, 3]
    assert next_permutation([5, 4, 3, 2, 1]) == False


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    result = next_permutation(a)
    if result:
        print(*result)
    else:
        print(-1)
