class Solution:
	def backPackII(self, m, A, V):
		s = [0] * (m + 1)
		for i in range(len(A)):
			for j in range(m,A[i]-1, -1):
				temp = s[j - A[i]] + V[i]
				s[j] = max(temp,s[j])
		return s[m]

solution  = Solution()
a = solution.backPackII(10,[2,3,5,7],[1,5,2,4])
print(a)