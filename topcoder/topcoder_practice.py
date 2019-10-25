def solve(a, b, c):
	global dp
	if (a, b, c) in dp:
		return dp[(a, b, c)]
	if c <= 1:
		return 3*min(b//2, a)
	if b <= 1:
		return 3*min(c//2, b)

	m1 = min(b//2, a)
	t1 = solve(a - m1, b-2*m1, c) + 3*m1
	m2 = min(b, c//2)
	t2 = solve(a, b-m2, c-2*m2) + 3*m2
	dp[(a, b, c)] = max(t1, t2)
	return dp[(a, b, c)] 

t = int(input())

for _ in range(t):
	a, b, c = map(int, input().split())
	dp = {}
	ans = solve(a, b, c)
	print(ans)
