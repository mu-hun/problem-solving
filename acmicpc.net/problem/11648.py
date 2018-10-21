# dic = {1:input()}

# def rec(sw = 1, c = 1):
# 	ke, sw = sw, 1
# 	_l = list(map(int, dic.get(ke, str(ke))))
# 	if len(_l) < 2 and ke is 1:
# 		print(0)
# 		return
# 	for i in _l:
# 		sw = sw * i
# 	if sw < 10:
# 		print(c)
# 		return c
# 	c = c + 1
# 	rec(sw, c)

# rec()

n, r = int(input()), 0
while n > 9:
	r += 1
	t = 1
	for i in str(n):
		t *= int(i)
	n = t
print(r)

