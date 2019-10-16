'''
Initially all time slots are individual slots. So the time slot returned is always maximum. 
When we assign a time slot ‘t’ to a job, we do union of ‘t’ with ‘t-1’ in a way that ‘t-1’ becomes parent of ‘t’. 
To do this we call union(t-1, t). 
This means that all future queries for time slot t would now return the latest time slot available for set represented by t-1.
'''

from functools import reduce

def find(s):
	global parent_arr
	# find the parent (max available slot for s)
	while s != parent_arr[s]:
		parent_arr[s] = parent_arr[parent_arr[s]]
		s = parent_arr[s]
	return s

def union(u, v):
	global parent_arr
	# make v as parent of u (i.e. update the max_available slot for v)
	parent_arr[v] = u

def job_sequencing(jobs, total_slots):	
	global parent_arr
	n = len(jobs)
	total_profit = 0
	for i in range(n):
		available_slot = find(jobs[i][1])
		if available_slot > 0:
			union(available_slot-1, available_slot)
			total_profit += jobs[i][0]
	return total_profit


jobs = [(15, 3), (20, 2), (12, 1), (35, 3), (5, 2), (30, 4), (25, 4)]	# (profit, deadline)
jobs.sort(reverse=True)
total_slots = reduce(lambda x,y: (x if x[1]>y[1] else y), jobs)[1]
parent_arr = [i for i in range(total_slots+1)]

ans = job_sequencing(jobs, total_slots)
print(ans)

