def substringCount(s: str, k: int):
    A = ord('a')

    MAX_CHAR = max(map(lambda char: ord(char) - A, set(list(s)))) + 1

    length = len(s)
    answer = 0

    def check(freq):
        for count in freq:
            if count and count != k:
                return False
        return True

    for i in range(length):
        counts = [0]*MAX_CHAR
        for j in range(i, length):
            char = ord(s[j]) - A
            counts[char] += 1
            if counts[char] > k:
                break
            if counts[char] == k and check(counts) == True:
                answer += 1
    return answer


def test_substring():
    assert substringCount('aabbcc', 2) == 6
    assert substringCount('aabccc', 2) == 3
