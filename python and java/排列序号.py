class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        # Write your code here
        sum = 1
        length = len(A)
        factor = 1
        for i in range(2,length + 1):
        	count = 0
        	for j in A[-i:]:
        		if j < A[-i]:
        			count = count + 1
        	sum = sum + count * factor
        	factor = factor * (i)
        return sum