#遍历方法，时间复杂度为o(n^2)，超过了时间限制
class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        max = nums[0]
        for i in range(0,len(nums)):
        	temp = nums[i]
        	if temp > max:
        		max = temp
        	for j in range(i + 1,len(nums)):
        		temp = temp * nums[j]
        		if temp > max:
        			max = temp
        return max



#动态规划方法，时间复杂度为o(n)
#首先需要三个变量，第一是以该点为末尾的子序列的乘积的最小值（之所以要记录这个数字，是因为有可能前面的是负数，乘以当前的就成为了正数。）
#第二个是以改点为末位的子序列的乘积的最大值。(求法是，要么是当前点，要么是当前点乘以前一个点为末位的序列的最大乘积)
#第三个变量是纪录到这个点为止，子序列的最大乘积。(也就是说可能最大乘积不包括当前的点，前两个变量都是肯定包含当前点的)
class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        maxPos = nums[0]
        maxNeg = nums[0]
        maxPlus = nums[0]
        for i in range(1,len(nums)):
        	tempMaxPos = maxPos
        	temMaxNeg = maxNeg
        	maxPos = max(nums[i],max(nums[i] * tempMaxPos, nums[i] * temMaxNeg))
        	maxNeg = min(nums[i],min(nums[i] * tempMaxPos, nums[i] * temMaxNeg))
        	maxPlus = max(maxPlus,maxPos)
        return maxPlus

solution = Solution()
print(solution.maxProduct([2,3,-2,4]))