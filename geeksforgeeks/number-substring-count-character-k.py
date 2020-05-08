def substringCount(s: str, k: int):
    A = ord('a')

    MAX_CHAR = max(map(lambda char: ord(char) - A, set(list(s)))) + 1

    length = len(s)
    count = 0

    def check(freq):
        for count in freq:
            if count > 0 and count != k:
                return False
        return True

    for i in range(length):
        freq = [0] * MAX_CHAR
        for j in range(i, length):
            index = ord(s[j]) - A
            freq[index] += 1
            if freq[index] > k:
                break
            if freq[index] == k and check(freq) == True:
                count += 1
    return count


def test_substring():
    assert substringCount('aabbcc', 2) == 6
    assert substringCount('aabccc', 2) == 3
