def three_array_sort(L: list):
    return sorted(L, key=int)


def test_three_array_sort():
    assert three_array_sort(['3', '1', '2']) == ['1', '2', '3']


if __name__ == "__main__":
    print(*three_array_sort(input().split()))
