def schedule(starts: list, ends: list):
    t, count = 0, 0
    pairs = sort_pair(make_pair(starts, ends))
    for pair in pairs:
        if t < pair[0]:
            count += 1
            t = pair[1]
    return count


def sort_ab(a, b):
    if a[1] == b[1]:
        return a[0] < b[0]
    return a[1] < b[1]


def sort_pair(pairs):
    n = len(pairs)
    while (n > 1):
        j = 0
        for i in range(1, n):
            if sort_ab(pairs[i], pairs[j]):
                tmp = pairs[i]
                pairs[i] = pairs[j]
                pairs[j] = tmp
        n -= 1
    return pairs


def make_pair(starts, ends):
    result = []
    for i in range(len(starts)):
        result.append([starts[i], ends[i]])
    return result


def test_schedule():
    assert schedule([1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12], [
        4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 4


if __name__ == "__main__":
    N = int(input())
    starts = [0]*N
    ends = [0]*N

    for i in range(N):
        starts[i], ends[i] = map(int, input().split())

    print(schedule(starts, ends))
