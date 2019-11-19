'''
problem_url -: https://leetcode.com/problems/path-with-maximum-gold/
Editorial-: https://leetcode.com/problems/path-with-maximum-gold/discuss/398282/JavaPython-3-BFS-and-DFS-w-comment-brief-explanation-and-analysis.
'''

# grid = [[0,6,0],[5,8,7],[0,9,0]]
grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]

m = len(grid); n = len(grid[0])

def dfs(i, j, sum):
	if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] <= 0:
		return sum
	sum += grid[i][j]
	grid[i][j] -= 1000
	mx = 0
	for x, y in [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]:
		mx = max(dfs(x, y, sum), mx)
	grid[i][j] += 1000
	return mx

ans = max(dfs(i, j, 0) for i in range(m) for j in range(n))
print(ans)