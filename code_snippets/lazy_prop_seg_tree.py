import math

n = 4

seg_len = 2**(math.ceil(math.log2(n))+1) - 1
seg_arr = [[0, 0] for i in range(seg_len)]	#[lights_off , lights_on]
lazy_arr = [0]*seg_len

def add(left, right):
	return [left[0]+right[0], left[1]+right[1]]

def construct(i, start, end):
	if start==end:
		seg_arr[i] = [1, 0]
	else:
		mid = start + end >> 1
		construct(2*i+1, start, mid)
		construct(2*i+2, mid+1, end)
		seg_arr[i] = add(seg_arr[2*i+1], seg_arr[2*i+2])
construct(0, 0, n-1)

def range_update(i, start, end, l, r):
	if lazy_arr[i]&1:
		seg_arr[i] = seg_arr[i][::-1]

		left = 2*i+1

		if left < seg_len:
			lazy_arr[left] += 1
			lazy_arr[left+1] += 1
		lazy_arr[i] = 0
	if r < start or end < l:
		return 
	if l <= start and end <= r:
		seg_arr[i] = seg_arr[i][::-1]
		left = 2*i+1

		if left < seg_len:
			lazy_arr[left] += 1
			lazy_arr[left+1] += 1

		return
	mid = start + end >> 1
	range_update(2*i+1, start, mid, l, r)
	range_update(2*i+2, mid+1, end, l, r)
	seg_arr[i] = add(seg_arr[2*i+1], seg_arr[2*i+2])

def range_query(i, start, end, l, r):
	if r < start or end < l:
		return [0, 0]
	if lazy_arr[i]&1:
		seg_arr[i] = seg_arr[i][::-1]
		left = 2*i+1

		if left < seg_len:
			lazy_arr[left] += 1
			lazy_arr[left+1] += 1
		lazy_arr[i] = 0
	if l <= start and end <= r:
		return seg_arr[i]
	mid = start + end >> 1
	left = range_query(2*i+1, start, mid, l, r)
	right = range_query(2*i+2, mid+1, end, l, r)
	return add(left, right)

range_update(0, 0, n-1, 0, 1)
range_update(0, 0, n-1, 1, 3)
q = range_query(0, 0, n-1, 1, 2)
range_update(0, 0, n-1, 1, 3)
q2 = range_query(0, 0, n-1, 0, 3)
print(q[1],q2[1])