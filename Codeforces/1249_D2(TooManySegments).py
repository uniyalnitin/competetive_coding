'''
Problem_url-: https://codeforces.com/contest/1249/problem/D2
Editorial-: https://codeforces.com/blog/entry/70779
'''
import sys
import heapq

def input():
	return sys.stdin.readline().strip()


maxn = 200005

BIT = [0]*maxn

def add(i, val):
	while i < maxn:
		BIT[i] += val
		i += (-i & i)

def read(i):
	ret = 0
	while i > 0:
		ret += BIT[i]
		i -= (-i & i)
	return ret 

points = [0]*maxn
segs = []

n, k = map(int, input().split())

for i in range(n):
	l, r = map(int, input().split())
	segs.append((l, r, i+1))
	points[l] += 1
	points[r+1] -= 1

cand = []
st = 0
for i in range(maxn):
	st += points[i]
	if st > k:
		cand.append((i, st-k))

segs.sort(key = lambda x:(x[0], x[1]))
pq = []
ans = []
j = 0
for i, v in cand:
	v = v - read(i)
	if v <= 0:
		continue
	while j < n and segs[j][0] <= i:
		heapq.heappush(pq, (-segs[j][1], segs[j][0], segs[j][2]))
		j += 1
	for _ in range(v):
		r, l, idx = heapq.heappop(pq)
		ans.append(idx)
		add(l, 1)
		add(-r+1, -1)
print(len(ans))
print(*ans)