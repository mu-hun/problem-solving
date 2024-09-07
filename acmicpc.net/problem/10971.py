from itertools import permutations
from math import inf


def main(graph: tuple[tuple[int]]):
    minimum = inf
    length = len(graph)

    indexes = range(length)

    for permutation in permutations(indexes[1:]):
        permutation = (0,) + permutation + (0,)
        total_weight = 0

        # range(len(permutation) - 1) = range(length)
        for index in indexes:
            weight = graph[permutation[index]][permutation[index + 1]]
            if weight == 0:
                total_weight = inf
                break
            total_weight += weight

        minimum = min(minimum, total_weight)

    return minimum


def test():
    assert main(((0, 10, 15, 20), (5, 0, 9, 10), (6, 13, 0, 12), (8, 8, 9, 0))) == 35


if __name__ == "__main__":
    print(main(tuple(tuple(map(int, input().split())) for __ in range(int(input())))))
