def solve_puzzle(mixed: list[list[str]]):
    answer = 0

    for column_index in range(len(mixed)):
        for row_index in range(len(mixed[column_index])):

            letter = mixed[column_index][row_index]

            if letter != '.' and solved_map[letter] != (column_index, row_index):
                answer += calculate_diff_count(letter,
                                               (column_index, row_index))

    return answer


def calculate_diff_count(letter: str, pos: tuple[int, int]):
    x, y = subtract_tuple(solved_map[letter], pos)

    return abs(x) + abs(y)


def subtract_tuple(tuple1: tuple[int, int], tuple2: tuple[int, int]):
    return tuple(map(lambda i, j: i - j, tuple1, tuple2))


solved_map = {'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3),
              'E': (1, 0), 'F': (1, 1), 'G': (1, 2), 'H': (1, 3),
              'I': (2, 0), 'J': (2, 1), 'K': (2, 2), 'L': (2, 3),
              'M': (3, 0), 'N': (3, 1), 'O': (3, 2)}


def test_calculate_diff_count():
    assert calculate_diff_count('N', (3, 2)) == 1


def test_cases():
    assert solve_puzzle(['ABCD', 'EFGH', 'IJKL', 'M.NO']) == 2
    assert solve_puzzle(['.BCD', 'EAGH', 'IJFL', 'MNOK']) == 6


if __name__ == '__main__':
    print(solve_puzzle([input() for __ in range(4)]))
