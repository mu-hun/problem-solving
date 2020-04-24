def check(freq, k):
    for char in freq:
        if(char and char != k):
            return False
    return True


def substringCount(s: str, k: int):
    count = 0

    MAX_CHAR = max(map(lambda x: ord(x) - ord('a'), [char for char in s])) + 1

    for i in range(0, len(s)):
        freq = [0] * MAX_CHAR
        for j in range(i, len(s)):
            index = ord(s[j]) - ord('a')
            freq[index] += 1
            if freq[index] > k:
                break
            if freq[index] == k and check(freq, k) == True:
                count += 1
    return count


def test_substring():
    assert substringCount('aabbcc', 2) == 6
    assert substringCount('aabccc', 2) == 3
