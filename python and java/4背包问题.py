# class Solution:
# 	def backPackVI(self, nums, target):
		
# 		s = [0] * (target + 1)
# 		s[0] = 1#当target为0，也就是容量只有0的解决方案只有一种，什么都不放

# 		for i in range(1,target + 1):
# 			for j in nums:
# 				if i >= j:
# 					s[i] = s[i] + s[i - j]

# 		return s[target]


class Solution:
	def backPackVI(self,nums,target):
		s = [0] * (target + 1)
		s[0] = 1
		nums.sort()#当target很大的时候，可以使用这种方法。也就是i已经小于数组里面的最小值了，后面也无需比较
		for i in range(1,target + 1):
			for j in nums:
				if i < j:
					break
				s[i] = s[i] + s[i - j]
		return s[target]


solution  = Solution()
a = solution.backPackVI([2,3,5,7],10)
print(a)