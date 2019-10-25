'''
problem_url-: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
editorial_url -: youtube-: similar approach https://www.youtube.com/watch?v=XHjjIJxnAJY
'''
A = [6, 2, 4]
dp = {}

def recur(start, end):
	if (start, end) in dp:
		return dp[(start, end)]
	if start == end:
		return A[start], 0

	local_max, local_sum = 0, float('inf')
	for i in range(start, end):
		left_max, left_sum = recur(start, i)
		right_max, right_sum = recur(i+1, end)

		local_max = max(local_max, max(left_max, right_max))
		local_sum = min(local_sum, left_sum + right_sum + left_max*right_max)

	dp[(start, end)] = local_max, local_sum
	return dp[(start, end)]

n = len(A)
ans = recur(0, n-1)[-1]
print(ans)
