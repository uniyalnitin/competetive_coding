graph = {
	1: [2, 3],
	2: [2, 4, 4],
	3: [1, 2,  5],
	4: [3, 6],
	5: [6],
	6: [3]
}

n = 6
m = 12

IN = [0]*(n + 1)
OUT = [0]*(n + 1)

solution = []

def countInOutDegrees():
	for from_vert in graph:
		for to_vert in graph[from_vert]:
			OUT[from_vert] += 1
			IN[to_vert] += 1

def graphHasEulerianPath():
	start_nodes, end_nodes = 0, 0

	for i in range(1, n+1):
		if OUT[i] - IN[i] > 1 or IN[i] - OUT[i] > 1: return False

		elif OUT[i] - IN[i] == 1: start_nodes += 1

		elif IN[i] - OUT[i] == 1: end_nodes += 1

	return (end_nodes == 0 and start_nodes == 0) or (end_nodes == 1 and start_nodes == 1)

def findStartNode():
	start = 0
	for i in range(1, n+1):
		if OUT[i] - IN[i] == 1: return i 

		if OUT[i] > 0: start = i 
	return start

def DFS(at):
	while OUT[at] > 0:
		OUT[at] -= 1
		next_edge = graph[at][OUT[at]]
		DFS(next_edge)
	solution.append(at)

def findEulerianPath():
	countInOutDegrees()

	if not graphHasEulerianPath(): return null

	DFS(findStartNode())

	if len(solution) != m: print("Disconnected graph")


findEulerianPath()
print(solution)
