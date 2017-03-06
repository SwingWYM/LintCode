# class Solution:
# 	def __init__(self):
# 		self.trip = 0

# 	def go(self, i, j, m, n, l):
# 		if i == m - 1 and j == n - 1:
# 			self.trip = self.trip + 1
# 			return
# 		elif i >= m or j >= n:
# 			return
# 		elif l[i][j] == 1:
# 			return
# 		else:
# 			self.go(i + 1, j, m, n,l)
# 			self.go(i, j + 1, m, n,l)

# 	def uniquePathsWithObstacles(self, l):
# 		m = len(l)
# 		n = len(l[0])
		
# 		self.go(0, 0, m, n,l)

# 		return self.trip

# solution = Solution()
# a = solution.uniquePathsWithObstacles([[0]])
# print(a)

class Solution:
	def uniquePathsWithObstacles(self,data):
		m = len(data)
		n = len(data[0])
		for i in range(m):
			for j in range(n):
				if i == 0:
					if data[i][j] == 1:
						data[i][j] = 0
					else:
						if j > 0 and data[i][j-1] == 0:
							data[i][j] = 0
						else:
							data[i][j] = 1
				else:
					if j == 0:
						if data[i][j] == 1:
							data[i][j] = 0
						else:
							if i > 0 and data[i-1][j] == 0:
								data[i][j] = 0
								# print(data[i][j],data[i][j-1])
							else:
								data[i][j] = 1
					else:
						if data[i][j] == 1:
							data[i][j] = 0
						else:
							if data[i-1][j] == 0 and data[i][j-1] == 0:
								data[i][j] = 0
							else:
								data[i][j] = data[i][j - 1] + data[i - 1][j]
		return data[m-1][n-1]

solution = Solution()
# a = solution.uniquePathsWithObstacles([[0,1,0],[0,0,0],[0,0,0]])
# a = solution.uniquePathsWithObstacles([[0,0],[0,0],[0,0],[1,0],[0,0]])
# a = solution.uniquePathsWithObstacles([[0]])
a = solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(a)