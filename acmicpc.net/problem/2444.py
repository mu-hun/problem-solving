def star(N: int):
    result = []
    cache = '*'
    result.append(' '*(N-1) + cache)
    for i in range(2, N+1):
        cache += '**'
        result.append(' ' * (N-i) + cache)

    result += result[:-1][::-1]

    return result


def test_star():
    assert star(5) == ['    *',
                       '   ***',
                       '  *****',
                       ' *******',
                       '*********',
                       ' *******',
                       '  *****',
                       '   ***',
                       '    *', ]
    assert star(3) == ['  *',
                       ' ***',
                       '*****',
                       ' ***',
                       '  *', ]


if __name__ == "__main__":
    for s in star(int(input())):
        print(s)
