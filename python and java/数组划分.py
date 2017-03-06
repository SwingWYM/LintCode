class Solution:
	def partitionArray(self, nums, k):	#一趟快排
		nums.insert(0,k)
		begin = 0
		end = len(nums) - 1
		while begin < end:
			while begin < end and nums[end] >= k:
				end = end - 1
			nums[begin] = nums[end]
			while begin < end and nums[begin] < k:
				begin = begin + 1
			nums[end] = nums[begin]
		nums[begin] = 2
		nums.pop(begin)
		return begin



solution = Solution()
result = solution.partitionArray([3,2,2,1],2)
print(result)