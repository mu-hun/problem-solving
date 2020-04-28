def solution(stock, dates, supplies, k):
    answer = 0
    count = 0
    while count < k:
        if len(dates) == 0:
            return answer

        stock -= 1
        count += 1

        dates_left = list(map(lambda date: date - count, dates))

        for index in range(len(dates_left)):
            if stock < dates_left[index]:
                stock += supplies[index-1]
                dates = dates[index:]
                supplies = supplies[index:]
                answer += 1
                break
            if stock == dates_left[index]:
                stock += supplies[index]
                dates = dates[index+1:]
                supplies = supplies[index+1:]
                answer += 1
                break
    return answer


def test_solution():
    assert solution(4, [4, 10, 15], [20, 5, 10], 30) == 2
