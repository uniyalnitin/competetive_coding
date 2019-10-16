def is_overlapping(job1, job2):
	return job1[0] < job2[1]

def weighted_job_scheduling(jobs):
	n = len(jobs)
	dp = [job[2] for job in jobs]
	for i in range(n):
		for j in range(i):
			if not is_overlapping(jobs[i], jobs[j]):
				dp[i] = max(dp[i], jobs[i][2]+dp[j])
	print(dp)
	return max(dp)


jobs= [[1, 2, 50],	# [start_time, end_time, profit]
		[3, 5, 20],
		[6, 19, 100],
		[2, 100, 200]]

jobs.sort(key = lambda x: x[1])

ans = weighted_job_scheduling(jobs)
print(ans)
