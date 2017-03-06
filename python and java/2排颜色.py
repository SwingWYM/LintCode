#解法1，快速排序，不使用k，时间复杂度o（nlogn）
# class Solution:
# 	def sort(self,colors,begin,end):
# 		if begin >= end:
# 			return
# 		m = self.partion(colors,begin,end)
# 		self.sort(colors,begin,m-1)
# 		self.sort(colors,m+1,end)
# 	def partion(self,colors,begin,end):
# 		m = colors[begin]
# 		while begin < end:
# 			while begin < end  and colors[end] >= m:
# 				end = end - 1
# 			colors[begin] = colors[end]
# 			while begin < end and colors[begin] <= m:
# 				begin = begin + 1
# 			colors[end] = colors[begin]
# 		colors[begin] = m
# 		return begin
# 	def sortColors2(self, colors, k):#快速排序
# 		begin = 0
# 		end = len(colors) - 1
# 		self.sort(colors,begin,end)
# 		return colors

#解法2，使用k，知道k就知道了数组中包含了哪些数字，时间复杂度小于o（nk）
# class Solution:
# 	def sort(self,colors,begin,end,i):
# 		parse = begin
# 		while begin <= end:
# 			if colors[begin] == i:
# 				temp = colors[parse]
# 				colors[parse] = colors[begin]
# 				colors[begin] = temp
# 				parse = parse + 1
# 				print('parse:',parse)
# 				print('begim:',begin,'end:',end)
# 			begin = begin + 1
# 		return parse
# 	def sortColors2(self,colors,k):
# 		begin = 0
# 		end = len(colors) - 1
# 		for i in range(1,k + 1):
# 			begin = self.sort(colors,begin,end,i)
# 			print(begin)
# 		return colors

#解法3，直接遍历，这种方法需要额外的空间，不符合题目条件
# class Solution:
# 	def sortColors2(self,colors,k):
# 		result = []
# 		for i in range(1,k + 1):
# 			for j in colors:
# 				if i == j:
# 					result.append(j)
# 		return result

#解法4，时间复杂度为o（n）
#color[i]存储在color[color[i]-1]的格子当中
class Solution:
	def sortColors2(self,colors,k):
		i = 0
		while i < len(colors):
			if colors[i] > 0:
				if colors[colors[i] - 1] > 0:
					temp = colors[i]#当前的位置
					colors[i] = colors[colors[i] - 1]
					colors[temp - 1] = -1
				else:
					colors[colors[i] - 1] = colors[colors[i] - 1] - 1
					colors[i] = 0
			else:
				i = i + 1
			print(colors)
		index = len(colors) - 1
		for a in range(0,len(colors))[::-1]:
			if colors[a] == 0:
				continue
			temp = -colors[a]
			for j in range(temp):
				colors[index] = a + 1
				index = index - 1
		return colors
			

solution = Solution()
result = solution.sortColors2([3,2,2,1,4], 4)
print(result)
