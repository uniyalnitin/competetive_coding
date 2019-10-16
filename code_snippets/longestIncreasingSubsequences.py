arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)

def lis(arr, n):
	lis = [1]*n
	for i in range(1, n):
		for j in range(i):
			if arr[j] < arr[i] and lis[i] < lis[j] + 1:
				lis[i] = lis[j] + 1
	return max(lis)

ans = lis(arr, n)
print(ans)