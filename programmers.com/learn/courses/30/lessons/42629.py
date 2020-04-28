import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    start = 0
    heap = []

    while stock < k:
        for index in range(start, len(dates)):
            if stock >= dates[index]:
                heapq.heappush(heap, -supplies[index])
                start = index+1
                continue
            break

        stock += heapq.heappop(heap) * -1
        answer += 1
    return answer


def test_solution():
    assert solution(4, [4, 10, 15], [20, 5, 10], 30) == 2
