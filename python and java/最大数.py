import functools
class Solution:
	def compare(self,x,y):
		if x + y > y + x:
			return -1
		else:
			return 1

	def largestNumber(self, num):
		result = ''
		for i in range(len(num)):
			num[i] = str(num[i])
#str可以将数字转换为对应的字符串形势，chr可以将ascll码转换为对应的字符
#sort和sorted的不同：
#1、使用形式：x.sort();y = sorted(x)
#2、sort在原列表上改变；sorted返回排序好的列表
#
#sorted和sort的用法：
#比较函数的使用：return的如果是1表示，这两个数要交换位置；内建有一个函数cmp，是生序排序，如果要排序的是一个复杂类型，可以给cmp传值，比如cmp(x[2],y[2])，cmp中的左边大于右边，表示x和y要换位置
#在python3中不能直接使用比较函数，取而代之的是key关键字，但key关键字中的函数只能传入一个参数
		key = functools.cmp_to_key(self.compare)
		nums = sorted(num, key = key)
		# num.sort(self.compare)
		# print(nums)
		if nums[0] == '0':
			return '0'
		for x in nums:
			result  = result + x
		return result
solution = Solution()
result = solution.largestNumber([0,12,121])
print(result)