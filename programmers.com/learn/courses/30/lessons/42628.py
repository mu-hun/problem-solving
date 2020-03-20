import heapq


def solution(scoville: list, k: int):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < k:
        try:
            heapq.heappush(scoville, heapq.heappop(
                scoville) + heapq.heappop(scoville) * 2)
        except IndexError:
            return -1
        count += 1

    return count


def test_solution():
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2
    assert solution([1, 2], 5) == 1
    assert solution([1], 5) == -1
