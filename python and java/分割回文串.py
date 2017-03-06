class Solution:
	temp = []
	def __init__(self):
		self.result = []
		self.temp

	def isRound(self,s):
		strlen = len(s)
		for i in range(strlen//2):
			if s[i] != s[strlen - i - 1]:
				return False
		return True

	def partition(self, s):
		if len(s) == 0:
			aresult = self.temp[:]#深拷贝的一种方式，并不是最完美的方式
			
			self.result.append(aresult)
			
			# return#可要可不要，因为当前层执行完了以后，肯定会返回上层执行
		for i in range(len(s)):
			substr = s[0:i + 1]
			sublen = len(substr)
			if self.isRound(substr):
				self.temp.append(substr)
				self.partition(s[i + 1:])
				self.temp.pop()
		return self.result
		
	
solution = Solution()
a = solution.partition('aabab')
print(a)

# def a():
# 	b = []
# 	a = []
# 	a.append(3)
# 	a.append(4)
# 	b.append(a)
# 	a.pop()
# 	return b
# print(a())
# class a:
# 	def __init__(self):
# 		self.b = []
# 		self.c = []

# 	def x(self):
# 		self.c.append('9')
# 		self.c.append('10')
# 		self.b.append(self.c)
# 		self.c.pop()
# 		return self.b

# y = a()
# print(y.x())
