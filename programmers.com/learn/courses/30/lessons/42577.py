def is_same(a, b):
    lenA = len(a)

    if lenA < len(b):
        return a == b[:lenA]
    return a == b


def solution(_phone_book):

    phone_book = sorted(_phone_book)
    book_range = len(phone_book)

    for first_index in range(book_range):
        for second in phone_book[first_index+1:]:
            if is_same(phone_book[first_index], second):
                return False

    return True


test_cases = [
    ['119', '97674223', '1195524421'],
    ['123', '456', '789'],
    ['578', '643', '32576', '658'],
    ['12', '123', '1235', '567', '88'],
    ['243', '24', '54356', '23', '456']
]


def test_case():
    assert solution(test_cases[0]) == False
    assert solution(test_cases[1]) == True
    assert solution(test_cases[2]) == True
    assert solution(test_cases[3]) == False
    assert solution(test_cases[4]) == False
