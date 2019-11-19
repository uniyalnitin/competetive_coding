'''
	Problem Url: https://www.hackerrank.com/challenges/bear-and-steady-gene/problem
	Idea: Sliding Window (Catter Piller Method)
'''

ip = open("testdata.txt", "r")

def input():
	return ip.readline().strip()

from collections import Counter

def balanced(n, dic):
	bal = True
	for k, v in dic.items():
		if v > n:
			bal = False
			break
	return bal

# Complete the steadyGene function below.
def steadyGene(gene):
	print(gene)
	N = len(gene)
	g_n = N/4
	gene_freq = Counter(gene)
	min_ans = 10**9
	l, r = 0, 0
	last = None
	while l < N and r < N:
		if not balanced(g_n, gene_freq):
			gene_freq[gene[r]] -= 1
			r += 1
		else:
			min_ans = min(min_ans, r - l)
			gene_freq[gene[l]] += 1
			l += 1
	return min_ans

n = int(input())
gene = input()
print(steadyGene(gene))