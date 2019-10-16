'''
sqrt decompositionn, Range sum query and point update
'''

	import math

arr = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10] # original array
n = len(arr)

blk_sz = int(math.sqrt(n)) 
block = [0]*(blk_sz+1) # decomposed array
        
def preprocess(arr, n):
	global block, blk_sz
	blk_idx = -1
	for i in range(n):
		if i%blk_sz == 0:
			blk_idx += 1
		block[blk_idx] += arr[i]

preprocess(arr, n)

def update(idx, val):
	global arr, block
	blk_idx = idx // blk_sz
	block[blk_idx] += val - arr[idx]
	arr[idx] = val

def query(l, r):
	# complexity O(sqrt(n))
	total = 0

	while l < r and l%blk_sz != 0 and l != 0:
		#traversing first block in range
		total += arr[l]
		l += 1

	while l + blk_sz <= r:
		# traversing completely overlapped blocks in range 
		total += block[l//blk_sz]
		l += blk_sz

	while l <= r:
		# traversing last block in range
		total += arr[l]
		l += 1
	return total

print(query(3, 8))
print(query(1, 6))
update(8, 0)
print(query(8, 8))