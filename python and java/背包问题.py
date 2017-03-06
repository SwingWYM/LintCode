class Solution:
	#s[i][j]表示：容量为i的时候，前j个物体的情况下，可以容下多少
	def backPack(self, m, A):
		s = [([] * (m + 1)) for i in range(len(A))]#背包容量为0,len(A)行，m+1列
		for i in range(len(A)):#所有容量m为0的情况，s[i][0] = 0
			s[i].append(0)
		for i in range(1,m + 1):
			if i > A[0]:
				s[0].append(A[0])
			else:
				s[0].append(0)#以上两步是判断能否容下第一个物体，这个值是后续计算的基础
			for j in range(1,len(A)):
				if i < A[j]:
					s[j].append(s[j - 1][i])
				else:
					s[j].append(max(s[j - 1][i], s[j - 1][i - A[j]] + A[j]))

		# print(s[len(A) - 1][m])
		# return s
		return s[len(A) - 1][m]

class Solution:
	def backPack(self, m, A):
		s = [0] * (m + 1)#只用一个一维数组，只要保证每次进行第i个判断的时候，数组中保存的是i－1判断完以后的值，故需要对m进行从大到小的遍历

			# for i in range(len(A)):
			# 	for j in range(m,-1,-1):
			# 		if A[i] > j:
			# 			break
			# 		else:
			# 			temp = s[j - A[i]] + A[i]
			# 			s[j] = max(temp,s[j])

		for i in range(len(A)):
			for j in range(m,A[i]-1,-1):#当前容量小于A[i]的情况不用更新
				temp = s[j - A[i]] + A[i]
				s[j] = max(temp,s[j])

		return s[m]


solution  = Solution()
a = solution.backPack(80000, [81,112,609,341,164,601,97,709,944,828,627,730,460,523,643,901,602,508,401,442,738,443,555,471,97,644,184,964,418,492,920,897,99,711,916,178,189,202,72,692,86,716,588,297,512,605,209,100,107,938,246,251,921,767,825,133,465,224,807,455,179,436,201,842,325,694,132,891,973,107,284,203,272,538,137,248,329,234,175,108,745,708,453,101,823,937,639,485,524,660,873,367,153,191,756,162,50,267,166,996,552,675,383,615,985,339,868,393,178,932])
print(a)