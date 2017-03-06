# class Solution:
# 	def threeSum(self, numbers):
# 		result = []
# 		l = len(numbers)
# 		for i in range(l):
# 			for j in range(l):
# 				if j > i:
# 					for k in range(l):
# 						if k > j and numbers[i] + numbers[j] + numbers[k] == 0 and (numbers[i] != 0 or numbers[j] != 0):
# 							temp = [numbers[i],numbers[j],numbers[k]]
# 							temp.sort()
# 							temp = tuple(temp)
# 							if temp not in result:
# 								result.append(temp)
# 		return result
# 		print(result)

class Solution:
	def threeSum(self, numbers):
		numbers.sort()#先对数组进行排序，就可以进行剪枝
		result = []
		l = len(numbers)
		for i in range(l):
			if numbers[i] > 0:#剪枝，这里可以剪枝是由于target的特殊性，如果target是一个负数，就不能这样剪枝。因为数组在当前元素后面可能还存在负数。
				break
			for j in range(l):
				if numbers[i] + numbers[j] > 0:#剪枝
					break
				if j > i:
					for k in range(l):
						if numbers[i] + numbers[j] + numbers[k] > 0:#剪枝
							break
						if k > j and numbers[i] + numbers[j] + numbers[k] == 0:
							temp = [numbers[i],numbers[j],numbers[k]]
							temp.sort()
							temp = tuple(temp)
							if temp not in result:
								result.append(temp)
		return result
		print(result)
		

solution = Solution()
result = solution.threeSum([1,2,33,23,2423,33,23,1,7,6,8787,5,33,2,3,-23,-54,-67,100,400,-407,-500,-35,-8,0,0,7,6,0,1,2,-56,-89])
print(result)