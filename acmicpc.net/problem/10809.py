def solution(string: str):
    check = [-1]*26
    for index in range(len(string)):
        checkIndex = ord(string[index]) - 97
        if check[checkIndex] != -1:
            continue
        check[checkIndex] = index
    return check


def test_solution():
    assert solution('baekjoon') == [1, 0, -1, -1, 2, -1, -1, -1, -1,
                                    4, 3, -1, -1, 7, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]


if __name__ == "__main__":
    print(' '.join(map(str, solution(input()))))
