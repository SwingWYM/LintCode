class Solution:
	#o(n)和o(不知道)
	# def majorityNumber(self,nums):
	# 	set = {}
	# 	count = 0
	# 	length = len(nums)
	# 	for x in nums:
	# 		if x in set:
	# 			set[x] = set[x] + 1
	# 		else:
	# 			set[x] = 1
	# 		if set[x] > count:
	# 			count = set[x]
	# 			result = x
	# 	if count > length/2:
	# 		return result
	# 	else:
	# 		return None


#o(n)and o(1)，  Moore’s Voting Algorithm
	def majorityNumber(self,nums):
		count = 1
		result = 0
		for i in range(1,len(nums)):
			if nums[i] == nums[result]:
				count = count + 1
			else:
				count = count - 1
			if count == 0:
				result = i
				count = 1
		for x in nums:
			if x == nums[result]:
				count = count + 1
		if count > len(nums)/2:
			return nums[result]

solution = Solution()
print(solution.majorityNumber([2,1,2,1,2]))