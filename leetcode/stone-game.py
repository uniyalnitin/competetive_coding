'''
problem_url -: https://leetcode.com/problems/stone-game/
editorail_url -: 1. Youtube-: https://www.youtube.com/watch?v=WxpIHvsu1RI&feature=youtu.be
				2: https://www.techiedelight.com/pots-gold-game-dynamic-programming/
'''

class Solution:
	def stoneGame(self, piles: List[int]) -> bool:
		n = len(piles)
		dp = [[0]*n for i in range(n)]
		
		for i in range(n):
			dp[i][i] = [piles[i], 0]
		
		for k in range(1, n):
			i = 0
			for j in range(k, n):
				if piles[i] + dp[i+1][j][1] > dp[i][j-1][1] + piles[j]:
					dp[i][j] = [dp[i+1][j][1] + piles[i], dp[i+1][j][0]]
				else:
					dp[i][j] = [dp[i][j-1][1] + piles[j], dp[i][j-1][0]]
				i += 1
		return dp[0][n-1][0] > dp[0][n-1][1]