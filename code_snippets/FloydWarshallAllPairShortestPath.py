import queue
import sys

# arr = [ [0,1,1,0],
# 		[0,0,0,1],
# 		[0,0,0,1],
# 		[1,0,0,0]]
arr = [ "0110",
		"0010",
		"0001",
		"1000"]

# arr = [ "0110",
# 		"0010",
# 		"1001",
# 		"1000"]

def get_neighbour(src):
	return [i for i in range(len(arr)) if arr[src][i]=='1']

def floyad_warshall(arr, n):
	distance = [[0]*n for i in range(n)]
	path = [[0]*n for i in range(n)]

	for i in range(n):
		for j in range(n):
			if arr[i][j]=='1':
				distance[i][j] = 1
				if i != j:
					path[i][j] = i 
			else:
				distance[i][j] = float('inf')
				path[i][j] = -1

	for k in range(n):
		for i in range(n):
			for j in range(n):
				if distance[i][k] == float('inf') or distance[k][j] == float('inf'):
					continue
				if distance[i][j] > distance[i][k] + distance[k][j] and i != j:
					distance[i][j] = distance[i][k]+ distance[k][j]
					path[i][j] = path[k][j]

	return distance, path

distance, path = floyad_warshall(arr, len(arr))
	
def print_path(path, start, end):
	stack = [end]
	while True:
		end = path[start][end]
		if end == -1:
			break
		stack.append(end)
		if end == start: break

	print(*stack[::-1])

print_path(path, 1, 3)