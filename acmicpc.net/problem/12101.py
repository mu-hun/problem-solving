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
        previous_items = memo_permutations[index - 1]

        current_items: list[item_type] = []

        for previous_item in previous_items:
            a = (*previous_item, 1)

            last_item = previous_item[-1]
            shifted = previous_item[:-1]

            b = (
                (*(shifted if len(shifted) > 0 else (1,)), last_item)
                if last_item + 1 > 3
                else (*shifted, last_item + 1)
            )

            current_items.append(a)
            current_items.append(b)

        memo_permutations.append(tuple(current_items))

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
