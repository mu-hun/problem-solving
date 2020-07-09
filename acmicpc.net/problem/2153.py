from math import sqrt, floor
import string

MAX = 1040


def sum_chars(word: str):
    words = {}
    value = 1
    for char in string.ascii_lowercase:
        words[char] = value
        value += 1
    for char in string.ascii_uppercase:
        words[char] = value
        value += 1
    result = 0
    for char in word:
        result += words[char]
    return result


def is_prime(number: int):
    check = [True]*(MAX+1)
    check[0] = False
    check[1] = True
    for i in range(2, floor(sqrt(MAX))+1):
        if check[i] == True:
            j = i*2
            while j <= MAX:
                check[j] = False
                j += i
    return check[number]


def solution(word: str):
    return is_prime(sum_chars(word))


def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(103) == True
    assert is_prime(100) == False


def test_solution():
    assert solution('UFRN') == True


if __name__ == "__main__":
    if solution(input()):
        print('It is a prime word.')
    else:
        print('It is not a prime word.')
