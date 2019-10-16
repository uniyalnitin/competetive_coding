jobs = [(3, 10, 20), (1, 2, 50), (6, 19, 100), (2, 100, 200)]	# start_time, end_time, profit
n = len(jobs)

def binary_search(jobs, n):
	l, h = 0, n-1

	while l <= h:
		mid = l + h >> 1

		if jobs[mid][1] <= jobs[n][0]:
			if jobs[mid+1][1] <= jobs[n][0]:
				l = mid + 1
			else:
				return mid
		else:
			h = mid - 1
	return -1

def find_max_profit(jobs, n):

	jobs.sort(key= lambda x: x[1])
	
	dp = [0]*n
	dp[0] = jobs[0][2]

	for i in range(1, n):
		incl_prof = jobs[i][2]
		l = binary_search(jobs, i)
		if l != -1:
			incl_prof += dp[l]
		dp[i] = max(incl_prof, dp[i-1])	# store maximum using including and excluding

	return dp[n-1]

ans = find_max_profit(jobs, n)
print(ans)