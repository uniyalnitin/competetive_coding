'''
	Problem url: https://www.codechef.com/NOV19B/problems/CAMC
	Editorial url: https://discuss.codechef.com/t/camc-editorial/43714
'''

t = int(input())

for _ in range(t):
	n, m = map(int, input().split())
	func = lambda x: (int(x[1]), x[0]%m)
	arr = list(map(func, enumerate(input().split())))
	arr.sort()

	cnt = [0]*m
	cnt0 = m; r = 0
	ans = float('inf')

	# Two Pointer Technique
	for l in range(n):
		while r < n and cnt0 > 0:
			cnt0 -= (cnt[arr[r][1]] == 0) # if next color (sliding in node) is not added yet (unexpolred)
			cnt[arr[r][1]] += 1
			r += 1
		if cnt0==0:	
			# if current window contain all the colors
			ans = min(ans, arr[r-1][0] - arr[l][0])

		# slide out the lth node from our window
		cnt[arr[l][1]] -= 1
		cnt0 += (cnt[arr[l][1]] == 0) # if the color at initial node (sliding out node) hasn't occured any where in Widow

	print(ans)