'''
KMP helps us in finding all prefixes of a string X in string Y.
'''
def computeTemporaryArray(pattern):
	lps = [0]*len(pattern)
	index = 0
	for i in range(1, len(pattern)):
		if pattern[i] == pattern[index]:
			lps[i] = index + 1
			index += 1
			i += 1
		elif index != 0:
			index = lps[index-1]
		else:
			lps[i] = 0
			i += 1
	return lps

def KMP(text, pattern):
	lps = computeTemporaryArray(pattern)
	print(lps)
	i, j = 0, 0
	while i < len(text) and j < len(pattern):
		if text[i] == pattern[j]:
			i += 1
			j += 1
		elif j != 0:
			j = lps[j-1]
		else:
			i += 1

	return j == len(pattern)

strr = "abcxabcdabcdabcy"
pattern = "abcdabcy"

result = KMP(strr, pattern)
print(result)