import sys
a = sorted([int(input()) for __ in range(9)])
total = sum(a)
for i in range(9):
	for j in range(i+1, 9):
		if total - a[i] - a[j] == 100:
			for k in range(9):
				if k == i or k == j:
					continue
				print(a[k])
			sys.exit(0)
