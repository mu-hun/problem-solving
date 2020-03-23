def calculate_coin(coins: list, goal):
    coins.reverse()
    count = 0
    for coin in coins:
        t = goal // coin
        goal -= t * coin
        count += t
    return count


def test_calculate_coin():
    assert calculate_coin([1, 5, 10, 50, 100, 500, 1000,
                           5000, 10000, 50000], 4200) == 6
    assert calculate_coin([1, 5, 10, 50, 100, 500, 1000,
                           5000, 10000, 50000], 4790) == 12


if __name__ == "__main__":
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    print(calculate_coin(coins, K))
