item_type = tuple[int, ...]


def get_permutation(n: int) -> tuple[item_type, ...]:
    memo_permutations: list[tuple[item_type, ...]] = [
        ((1,),),
        ((1, 1), (2,)),
        ((1, 2), (1, 1, 1), (2, 1), (3,)),
    ]

    if n <= len(memo_permutations):
        return tuple(memo_permutations[n - 1])

    for index in range(len(memo_permutations), n):
        current_permutation: list[item_type] = []

        for perm in memo_permutations[index - 1]:
            current_permutation.append((*perm, 1))

        for perm in memo_permutations[index - 2]:
            current_permutation.append((*perm, 2))

        for perm in memo_permutations[index - 3]:
            current_permutation.append((*perm, 3))

        memo_permutations.append(tuple(current_permutation))

    return tuple(
        sorted(set(memo_permutations[-1]), key=lambda iter: "".join(map(str, iter)))
    )


def test_get_permutation():
    assert get_permutation(3) == ((1, 2), (1, 1, 1), (2, 1), (3,))
    assert get_permutation(4) == (
        (1, 1, 1, 1),
        (1, 1, 2),
        (1, 2, 1),
        (1, 3),
        (2, 1, 1),
        (2, 2),
        (3, 1),
    )


if __name__ == "__main__":
    N, K = map(int, input().split())
    permutation = get_permutation(N)
    print("+".join(map(str, permutation[K - 1])) if len(permutation) >= K else -1)
