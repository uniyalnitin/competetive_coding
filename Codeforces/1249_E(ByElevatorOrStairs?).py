'''
problem_url-: https://codeforces.com/contest/1249/problem/E
editorial -: https://codeforces.com/blog/entry/70779

Idea-: Let dp[i,0] be the minimum required time to reach the floor i if we not in the elevator right now and dp[i,1] 
	be the minimum required time to reach the floor i, if we in the elevator right now.
	Initially, all values in dp are +∞, except dp[1,0] = 0 and dp[1,1] = c
'''
import sys

def input():
	return sys.stdin.readline().strip()

MAX = pow(10, 9)

n, c = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[MAX]*2 for _ in range(n)]
dp[0] = [0, c]

for i in range(n-1):
	dp[i+1][0] =  min(dp[i+1][0], dp[i][0]+A[i])
	dp[i+1][0] =  min(dp[i+1][0], dp[i][1]+A[i])
	dp[i+1][1] =  min(dp[i+1][1], dp[i][0]+B[i] + c)
	dp[i+1][1] =  min(dp[i+1][1], dp[i][1]+B[i])

for i in range(n):
	print(min(*dp[i]), end=" ")