import heapq
import copy


def fuel_fill(stations: int, goal: int, tank: int, location: list, amount: list):
    currect = 0
    heap = copy.deepcopy(amount)

    ans = 0

    heapq._heapify_max(heap)

    for index in range(stations):
        distance = location[index] - currect

        while tank - distance < 0:
            if len(heap) == 0:
                return -1
            tank += heapq.heappop(heap)
            ans += 1

        tank -= distance
        currect = location[index]
        heapq.heappush(heap, amount[index])

    left = goal - currect

    while tank - left < 0:
        if len(heap) == 0:
            return -1
        tank += heapq.heappop(heap)
        ans += 1

    return ans


def test_fuel_fill():
    assert fuel_fill(4, 25, 10, [10, 14, 20, 21], [10, 5, 2, 4]) == 2
    assert fuel_fill(4, 25, 10, [4, 5, 11, 15], [4, 2, 5, 10]) == 3
