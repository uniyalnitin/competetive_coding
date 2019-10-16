A = ['b','a' ,'d']
B = ['a', 'b', 'c', 'd']

n, m = len(A), len(B)

# longest common subsequence (top down)
# i: pointer to string A
# j: pointer to string B
def lcs_recursion(i, j):
	if i==n or j==m:
		return 0
	elif A[i]==B[j]:
		return 1 + lcs_recursion(i+1, j+1)
	else:
		return max(lcs_recursion(i+1, j), lcs_recursion(i, j+1))


# Dynamic approach (bottom up)

dp = [[0]*(m+1) for i in range(n+1)]

def lcs_dynamic():
	for i in range(1, n+1):
		for j in range(1, m+1):
			if A[i-1]==B[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return dp[n][m]

ans = lcs_dynamic()
print(ans)