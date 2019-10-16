jobs = [(3, 10, 20), (1, 2, 50), (6, 19, 100), (2, 100, 200)]	# start_time, end_time, profit
n = len(jobs)

def latest_non_conflict(arr, i):
	for j in range(i-1, -1, -1):
		if arr[j][1] <= arr[i-1][0]:
			return j 
	return -1

def find_max_profit_recur(arr, n):
	if n==1: return arr[n-1][2]
	incl_profit = arr[n-1][2]

	i = latest_non_conflict(arr, n)

	if i != -1:
		incl_profit += find_max_profit_recur(arr, i+1)
	excl_profit = find_max_profit_recur(arr, n-1)

	return max(incl_profit, excl_profit)


def find_max_profit(jobs, n):

	jobs.sort(key= lambda x: x[1])
	return find_max_profit_recur(jobs, n)

ans = find_max_profit(jobs, n)
print(ans)