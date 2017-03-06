class Solution:
	def median(self,nums):
		nums.sort();
		return nums[len(nums)//2 if len(nums) % 2 != 0 else len(nums)//2 - 1]

solution = Solution()
print(solution.median([2,1,3,5,6]))