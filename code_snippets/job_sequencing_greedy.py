from functools import reduce

def job_sequencing(jobs, total_slots):
	n = len(jobs)
	slots = [0]*total_slots

	total_profit = 0
	for i in range(n):
		#palce the ith job in the slot if available
		for j in range(jobs[i][1]-1, -1, -1):
			if slots[j]==0:
				slots[j]=1
				total_profit += jobs[i][0]
				break
	return total_profit

jobs = [(15, 3), (20, 2), (12, 1), (35, 3), (5, 2), (30, 4), (25, 4)]	# (profit, deadline)
jobs.sort(reverse=True)

total_slots = reduce(lambda x,y: (x if x[1]>y[1] else y), jobs)[1]
ans = job_sequencing(jobs, total_slots)
print(ans)

