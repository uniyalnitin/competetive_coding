'''
Range Minimum Query using sparse table
'''

import math

arr = [2, 4, 3, 1, 6, 7, 8, 9, 0, 7]
n = len(arr)

# M[i][j] = index of minimum value in the subarray arr[i: i+ 2^j] starting at i having length 2^j
M = [[0]*(int(math.log2(n))+1) for i in range(n)]	# M[0, n][0, log2(n)]


def preprocess(M, arr, n):
	'''
	Generate the sparse table in O(n*log(n)) time and space complexity for Range Minimum Query
	M[i][j] => minimum value in the first half and second half of the interval
	M[i][j] = M[i][j-1] if arr[M[i][j-1]] <= arr[M[i + 2^(j-1) - 1][j - 1]] else M[i + 2^(j-1) -1][j-1]
	'''

	for i in range(n):
		# initialize M for the intervals with length 1
		M[i][0] = i

	for j in range(1, int(math.log2(n))+1):	# column range
		i = 0
		while i + (1 << j) - 1 < n:	# i + 2^j < n (2^j length of elements)
			M[i][j] = M[i][j-1] if arr[M[i][j-1]] <= arr[M[i + (1 << (j-1))][j - 1]] else M[i + (1 << (j-1))][j-1]	# interval comparision
			i += 1

def rangeMinQuery(i, j):
	'''
	time complexity = O(1)
	idea: select two blocks such that entirely cover the interval [i, j] and find minimum between them
	k = log(j - i + 1) => length of the blocks
	first block starting from i of length 2^k in right to i (-->)
	second block starting from j of length 2^k in left to j-1 (<--)
	'''
	k = int(math.log2(j - i + 1))

	return M[i][k] if arr[M[i][k]] <= arr[M[j - (1 << k)][k]] else M[j - (1 << k)][k]

preprocess(M, arr, n)
# print(M)
ans = rangeMinQuery(2, 7)
print(ans)