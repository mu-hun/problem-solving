def rotLeft(array, rotateTo):
    odd = rotateTo % len(array)
    for _ in range(odd):
        poped = array.pop(0)
        array = [*array, poped]
    return array


def test_rotLeft():
    assert rotLeft([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4]
