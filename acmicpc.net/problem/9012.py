def check(string):
    stack = []
    for j in string:
        if j is '(':
            stack.append(j)
        elif j is ')':
            if stack == []:
                return False
            stack.pop()
    return stack == []


def test_check():
    assert check('(())())') == False
    assert check('(((()())()') == False
    assert check('(()())((()))') == True
    assert check('((()()(()))(((())))()') == False
    assert check('()()()()(()()())()') == True
    assert check('(()((())()(') == False


if __name__ == "__main__":
    for i in [input() for i in range(int(input()))]:
        if check(i):
            print('YES')
        else:
            print('NO')
