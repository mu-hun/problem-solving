n, r = int(input()), 0
while n > 9:
	r += 1
	t = 1
	for i in str(n):
		t *= int(i)
	n = t
print(r)

