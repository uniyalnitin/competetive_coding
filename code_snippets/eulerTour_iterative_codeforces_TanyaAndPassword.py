'''
problem link-: https://codeforces.com/contest/508/problem/D

editorial - :
At first, let's convert data from input in directed graph. Vertexes in this graph will all strings 
with length equals to 2 and consisting of uppercase and lowercase letters of the latin alphabet. For all 3-letters 
strings from input — si's, let's add edge from vertex si[0]si[1] to si[1]si[2].

Now we need to find in this graph Euler path. For this we can use Fleury's algorithm. It is worth noting, that Euler
path consists, if count of vertexes, in wich in-degree and out-degree differs by one, less then 3, and in-degree and 
out-degree of others vertexes — even. If we can't find Euler path — print NO. Asymptotic behavior of this solution — O(m), 
where m — count of different 3-letters strings from input. It equals to number of edges in graphs
'''

import sys
from collections import defaultdict, Counter

def q() :
    print("NO")
    exit()

N = int(sys.stdin.readline())
node = defaultdict(list)
counter = Counter()
for i in range(N) :
	s = sys.stdin.readline()
	n1,n2 = s[:2],s[1:3]
	if i == 0 : start = n1
	node[n1].append(n2)
	counter[n1]+=1
	counter[n2]-=1
	
st = en = False
for key, val in counter.items():
	if val > 1: q()
	if val == 1:
		if st: q()
		st, start = True, key
	if val == -1:
		if en: q()
		en  = True

if st != en: q()
S =  [start]
ans = []

while S:
	s = S[-1]
	if node[s]:
		S.append(node[s].pop())
	else:
		S.pop()
		ans.append(s[1])
ans.append(start[0])
ans.reverse()

if len(ans) == N+2 :
	print("YES")
	print("".join(ans))
else : 
	print("NO")