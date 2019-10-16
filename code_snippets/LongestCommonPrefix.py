# Use built-inall() and startswith() functions. 
# It first finds the shortest word in the input array, 
# then it iterates each character of the shortest word to 
# find out whether the character is common to the rest of words.

# def longestCommonPrefix(self, strs):
#     longest_pre = ""
#     if not strs: return longest_pre
#     shortest_str = min(strs, key=len)
#     for i in range(len(shortest_str)):
#         if all([x.startswith(shortest_str[:i+1]) for x in strs]):
#             longest_pre = shortest_str[:i+1]
#         else:
#             break
#     return longest_pre


# Binary search on the length of the prefix on the first word of the input array. 
# isCommonPrefix() function test whether a given length of the first word produces a 
# common prefix for all words in the array.

# def longestCommonPrefix(strs):
#     def isCommonPrefix(strs, length):
#         # has to put 0 in the strs index
#         strl = strs[0][:length]
#         print(strl)
#         if not all(strs[i].startswith(strl) for i in range(1, len(strs))):
#         	return False
#         return True

#     if not strs: return ""
#     minLen = len(min(strs, key=len))
#     low, high = 1, minLen
#     # the binary search on the length of prefix on the first word
#     while(low<=high):
#         mid = (low+high) // 2
#         if (isCommonPrefix(strs, mid)):
#             low = mid + 1
#         else:
#             high = mid - 1
#     return strs[0][:high]


# Divide and conquer, the intuition is LCP(W1,W2,W3...Wn) = LCP(LCP(W1,W2...Wk-1),LCP(Wk,Wk+1...Wn))


# def longestCommonPrefix(self, strs):
#     def commonPrefix(left,right):
#         min_len = min(len(left), len(right))
#         for i in range(min_len):
#             if left[i] != right[i]:
#                 return left[:i]
#         return left[:min_len]

#     def find_longestCommonPrefix(strs, left_index, right_index):
#         if left_index == right_index:
#             return strs[left_index]
#         # recursive call
#         else:
#             mid_index = (left_index + right_index)//2
#             lcpLeft = find_longestCommonPrefix(strs,left_index, mid_index)
#             lcpRight = find_longestCommonPrefix(strs,mid_index+1,right_index)
#             return commonPrefix(lcpLeft,lcpRight)

#     if not strs: return ""
#     return find_longestCommonPrefix(strs, 0, len(strs)-1)


# Python has a built-in commonprefix()function to solve the problem in single-line

# import os

# def longestCommonPrefix(strs):
	# return os.path.commonprefix(strs)


# strs = ["flower", "flame", "flavour"]

# ans = longestCommonPrefix(strs)
# print(ans)

