class Solution:
	def fourSum(self ,numbers, target):
		numbers.sort()
		lenth = len(numbers)
		result = []
		for i in range(lenth):
			if numbers[i] > abs(target):
				break
			for j in range(i + 1,lenth):
				if numbers[i] + numbers[j] > abs(target):
					break
				left = j + 1
				right = lenth - 1
				while left < right:
					sum = numbers[i] + numbers[j] + numbers[left] + numbers[right]
					if sum == target:
						temp = [numbers[i],numbers[j],numbers[left],numbers[right]]
						temp.sort()
						if temp not in result:
							result.append(temp)
						left = left + 1
						right = right - 1
					elif sum < target:
						left = left + 1
					else:
						right = right - 1
		return result

solution = Solution()
result = solution.fourSum([-8,-0,-7,-101,-123,-1,-2,1,1,4,-2,0,-1,0,-1111,0,-1,-2,-3,-4,-5,-6,-100,-98,-111,-11], -111)
print(result)