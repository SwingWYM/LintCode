class Solution:
	def subarraySumClosest(self, nums):
		#先进行排序，快排.
		lenth = len(nums)
		obj = {}
		temp = 0
		dif = abs(nums[0])
		result = [0,0]
		for i in range(0,lenth):
			temp = temp + nums[i]
			obj[i] = temp
		obj= sorted(obj.items(), key=lambda d:d[1])
		for i in range(len(obj)):
			if abs(obj[i][1])  < dif:
				dif = abs(obj[i][1])
				result[0] = 0
				result[1] = obj[i][0]
			if i - 1 < 0:
				continue
			if abs(obj[i][1] - obj[i - 1][1]) < dif:
				dif = abs(obj[i][1] - obj[i - 1][1])
				if obj[i][0] > obj[i - 1][0]:
					result[0] = obj[i - 1][0] + 1
					result[1] = obj[i][0]
				else:
					result[0] = obj[i][0] + 1
					result[1] = obj[i - 1][0]
		return result


solution = Solution()
result = solution.subarraySumClosest([-3, 1, 1, -3, 5])
print(result)