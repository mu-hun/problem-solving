from typing import Tuple


def is_right_triangle(lines: Tuple[int, int, int]):
    length = len(lines)
    maxIndex = 0
    for index in range(length):
        if lines[maxIndex] < lines[index]:
            maxIndex = index

    A = lines[(maxIndex + 1) % length]
    B = lines[(maxIndex - 1 + length) % length]

    return (A**2) + (B**2) == lines[maxIndex] ** 2


def test_is_right_triangle():
    assert is_right_triangle((6, 8, 10)) == True
    assert is_right_triangle((25, 52, 60)) == False
    assert is_right_triangle((5, 12, 13)) == True


if __name__ == "__main__":
    while True:
        lines = input()
        if lines == '0 0 0':
            break
        if is_right_triangle(tuple(map(int, lines.split()))):
            print('right')
        else:
            print('wrong')
