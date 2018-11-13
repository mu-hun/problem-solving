def check(_list):
	stack = []
	for j in _list:
		if j is '(':
			stack.append(j)
		elif j is ')':
			if stack == []:
				return False
			stack.pop()
	return stack == []

for i in [input() for i in range(int(input()))]:
	if check(i):
		print('YES')
	else:
		print('NO')
