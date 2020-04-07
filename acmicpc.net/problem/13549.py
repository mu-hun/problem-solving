from collections import deque

MAX = 200000


def find(n: int, m: int):
    c = [False] * MAX
    d = [-1] * MAX
    d[n] = 0

    q = deque()
    q_next = deque()

    q.append(n)

    while q:
        now = q.popleft()

        if now * 2 < MAX and c[now*2] == False:
            q.appendleft(now * 2)
            c[now * 2] = True
            d[now * 2] = d[now]

        if now - 1 >= 0 and c[now - 1] == False:
            q_next.append(now - 1)
            c[now - 1] = True
            d[now - 1] = d[now] + 1

        if now + 1 < MAX and c[now + 1] == False:
            q_next.append(now + 1)
            c[now + 1] = True
            d[now + 1] = d[now] + 1

        if not q:
            q = q_next
            q_next = deque()

    return d[m]


def test_find():
    assert find(4, 12) == 1
    assert find(2, 14) == 1
    assert find(5, 17) == 2
    assert find(5, 100000) == 5


if __name__ == "__main__":
    print(find(*map(int, input().split())))
