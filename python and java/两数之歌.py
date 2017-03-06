class Solution:
	def twoSum(self, numbers, target):
		i = 0
		j = 1
		l = len(numbers)
		while i < l:
			j = i + 1
			while j < l:
				if numbers[i] + numbers[j] == target:
					return [i + 1,j + 1]
				j = j + 1
			i = i + 1


solution = Solution()
result = solution.twoSum([1,0,-1,-1], -2)
print(result)