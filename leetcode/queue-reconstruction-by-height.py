'''
problem_url -: https://leetcode.com/problems/queue-reconstruction-by-height/
Editorial-: 1. sort the people in descending order of heights and p[1] (i.e. no. of people in front of this person
															 			who have a height greater than or equal to h)
			2. start inserting people at index == p[1] 

[[7,0]] (insert [7,0] at index 0)
[[7,0],[7,1]] (insert [7,1] at index 1)
[[7,0],[6,1],[7,1]] (insert [6,1] at index 1)
[[5,0],[7,0],[6,1],[7,1]] (insert [5,0] at index 0)
[[5,0],[7,0],[5,2],[6,1],[7,1]] (insert [5,2] at index 2)
[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] (insert [4,4] at index 4)
'''

def reconstructQueue(people):
	people.sort(key = lambda x: (-x[0], x[1]))
	res = []
	for p in people:
		res.insert(p[1], p)
	return res

people = [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
print(reconstructQueue(people))