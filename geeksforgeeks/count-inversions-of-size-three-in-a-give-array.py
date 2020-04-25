MAX_ITEM_SIZE = 10**100000


def is_inversion(L: list):
    prev = MAX_ITEM_SIZE
    for item in L:
        if item < prev:
            prev = item
            continue
        return False
    return True


def count_inversion(L: list):
    answer = []
    arr_len = len(L)

    def go(index: int, sub_array: list):
        print(sub_array)
        if len(sub_array) == 3:
            if is_inversion(sub_array):
                answer.append(sub_array)
            return
        if index == arr_len:
            return
        go(index+1, [*sub_array, L[index]])
        go(index+1, sub_array)

    go(0, [])

    return len(answer)


def test_inversion():
    assert count_inversion([4, 1, 3, 2, 5]) == 1
    assert count_inversion([15, 10, 1, 7, 8]) == 3
