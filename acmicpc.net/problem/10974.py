# refer: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True

_list = [i + 1 for i in range(int(input()))]

for i in _list:
	exc_list = [j for j in _list if not j is i]
	print(i, ' '.join(map(str, exc_list)))
	while next_permutation(exc_list):
		print(i, ' '.join(map(str, exc_list)))
