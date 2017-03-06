# class Solution:
# 	def __init__(self):
# 		self.trip = 0

# 	def go(self, i, j, m, n):
# 		if i == m - 1 and j == n - 1:
# 			self.trip = self.trip + 1
# 			return
# 		elif i >= m or j >= n:
# 			return
# 		else:
# 			self.go(i + 1, j, m, n)
# 			self.go(i, j + 1, m, n)

# 	def uniquePathis(self, m, n):
		
# 		self.go(0, 0, m, n)

# 		return self.trip

class Solution:
	def uniquePathis(self,m,n):
		p = []
		
		for i in range(m):
			p.append([1])
		for i in range(n - 1):
			# print(i)
			p[0].append(1)

		for i in range(1,m):
			for j in range(1,n):
				p[i].append(p[i][j-1] + p[i-1][j])

		return p[m-1][n-1]

solution = Solution()
a = solution.uniquePathis(3,3)
print(a)