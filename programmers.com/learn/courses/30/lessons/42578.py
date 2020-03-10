def solution(clothes: list):
    reduced = {}
    for target in clothes:
        if reduced.get(target[1]):
            reduced[target[1]] += 1
        else:
            reduced[target[1]] = 1

    result = 1
    for value in reduced.values():
        result *= value + 1

    return result - 1


def test_solution():
    assert solution([['yellow_hat', 'headgear'],
                     ['blue_sunglasses', 'eyewear'],
                     ['green_turban', 'headgear']]) == 5
    assert solution([
        ['crow_mask', 'face'],
        ['blue_sunglasses', 'face'],
        ['smoky_makeup', 'face']
    ]) == 3
