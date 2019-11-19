'''
	Problem Url: https://www.hackerrank.com/challenges/jeanies-route/problem
	Youtube Link: https://www.youtube.com/watch?v=ph-jcosp05k
	
	SUM = total distance between all included nodes
	M = distance between the farthest included nodes
	Formula = 2*SUM - M

	Run DFS from any desired city, For every node get the largest and 2nd largest distant desired city if any else 0
	Update the answer accordingly
'''


stdin = open("testdata.txt", "r")
# from sys import stdin

def input():
	return stdin.readline().strip()

import sys
from collections import defaultdict as ddict
import pdb;
sys.setrecursionlimit(10**9)

def jeanisRoute(k, roads, cities):
	g, start, cities = ddict(ddict), cities[0], set(cities)
	for i,j , w in roads:
		g[i][j] = g[j][i] = w 
	visited = set()
	ans = [0, 0]	# 2*total distance between all included nodes, distance between maximum distanct node
	def dfs(city, dis = 0):
		visited.add(city)
		isBelong = city in cities
		minus = [0,0]
		for adj_city, val in g[city].items():
			if adj_city not in visited:
				d = dfs(adj_city, dis+val) - dis # distance between current node and child's included node
				if d > 0:	# if there is included node in the path
					isBelong = True	# current node will also belong the answer 
					ans[0] += 2 * g[city][adj_city]	
					if d > minus[0]:
						minus[1], minus[0] = max(minus), d # update the largest and second largest distant included nodes from current node
					else: minus[1] = max(minus[1], d)

		ans[1] = max(ans[1], sum(minus)) #update the largest distance between any two desired city
		return dis + max(minus) if isBelong else 0	# return the farthest desired node total distance
	dfs(start) 
	return ans[0] - ans[1]

n, k = map(int, input().split())
cities = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(n-1)]

ans = jeanisRoute(k, roads, cities)
print(ans)