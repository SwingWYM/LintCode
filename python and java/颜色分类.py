class Solution:
	def sortColors(self,nums):#总共只有三种值，且在原数组上排序，那么使用快速排序，一趟就可以解决问题
		begin = 0
		end = len(nums) - 1
		i = 0
		while i <= end:
			if nums[i] == 0:
				temp = nums[begin]
				nums[begin] = nums[i]
				nums[i] = temp
				begin = begin + 1
				i = i + 1
			elif nums[i] == 2:
				temp = nums[end]
				nums[end] = nums[i]
				nums[i] = temp
				end = end - 1
			else:
				i = i + 1
		return nums
			


		

solution = Solution()
result = solution.sortColors([1, 0, 1, 2])
print(result)