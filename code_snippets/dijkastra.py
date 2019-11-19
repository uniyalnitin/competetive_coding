import heapq
# graph store the adjacency list of neighbour and its distance 

def dijkastra(graph, src):
	distances = {vertex:float('inf') for vertex in graph}
	distances[src] = 0
	'''
	When the distance to a vertex that is already in the queue is reduced, 
	we wish to update the distance and thereby move it to the front of the queue. 
	We accomplish this by maintaining a mapping of vertices to entries in our queues as entry_lookup. 
	When we wish to update the distance to a vertex, we retrieve the entry from entry_lookup and update the 0-th item in the list.
	'''
	entry_lookup = {}
	pq = []
	#push all the vertex in priority queue
	for vertex, distance in distances.items():
		entry =  [distance, vertex]
		entry_lookup[vertex] = entry
		heapq.heappush(pq, entry)
	while len(pq)>0:
		cur_dist, cur_vertex = heapq.heappop(pq)
		for neighbour, neighbour_distance in graph[cur_vertex].items():
			distance = distances[cur_vertex] + neighbour_distance
			if distance < distances[neighbour]:
				distances[neighbour] = distance
				entry_lookup[neighbour][0] = distance #update the mapped vertex distance (pq has the reference of the mapped vertex)
	return distances

example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(dijkastra(example_graph, 'X'))

# This is similar to BFS, but with priority que
def dijkastra_alter(graph, src):
	distances = {vertex: float('inf') for vertex in graph}
	pq = []

	distances[src] = 0

	heapq.heappush(pq, [distances[src], src])	# distance, node

	while pq:
		cur_dist, cur_vert = heapq.heappop(pq)
		for neigh, neigh_dist in graph[cur_vert].items():
			new_dist = cur_dist + neigh_dist
			if distances[neigh] > new_dist:
				distances[neigh] = new_dist
				heapq.heappush(pq, [new_dist, neigh])
	return distances

print(dijkastra_alter(example_graph, 'X'))