import sys
serises = [0 for __ in range(10001)]

for i in range(int(input())):
	serises[int(sys.stdin.readline())] += 1

for i in range(10001):
	if not serises[i] is 0:
		for j in range(serises[i]):
			print(i)
