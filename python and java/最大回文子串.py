#o(n^3)
# class Solution:

# 	def isRound(self,s):
# 		for i in range(len(s) // 2):
# 			if s[i] != s[len(s) - 1 - i]:
# 				return False
# 		return True
	
# 	def longestPalindrome(self,s):
# 		leng = 0
# 		substr = ''
# 		for i in range(len(s)):
# 			for j in range(i+1,len(s) + 1):
# 				if self.isRound(s[i:j]) and leng < j - i:
# 					leng = j - i
# 					substr = s[i:j]
# 		return substr
			


# l = [1,2,34]
# print(l[2:3])

# class Solution:
	
# 	def longestPalindrome(self, s):
# 		leng = 1
# 		substr = ''
# 		for i in range(len(s)):
# 			k = 0
# 			while i - k != -1 and i + k < len(s):
# 				if s[i - k] != s[i + k]:
# 					break
# 				else:
# 					if 2 * k + 1 > leng:
# 						leng = leng + 2 * k
# 						substr = s[i - k:i + k + 1]
# 				k = k + 1
# 			# print('1',substr)
# 			k = 0
# 			if i < len(s) - 1 and s[i] == s[i + 1]:
# 				while i - k != -1 and i + k + 1 < len(s):
# 					if s[i - k] != s[i + k + 1]:
# 						break
# 					else:
# 						if 2 * k + 2 > leng:
# 							leng = 2 * k + 2
# 							substr = s[i - k:i + k + 2]
# 					k = k + 1
# 			# print('2',substr)
# 		return substr
		
class Solution:
	
	def longestPalindrome(self, s):
		nwestr = ['#']
		p = []
		substrlen = 0
		substr = 0
		result = []
		maxright = 0
		maxright_i = 0
		for i in s:
			nwestr.append(i)
			nwestr.append('#')

		

		for i in range(len(nwestr)):
			if i < maxright:
				p.append(min(p[2 * maxright_i - i], maxright - i))
			else:
				p.append(1)
			while i - p[i] != -1 and i + p[i] < len(nwestr):
				if nwestr[i - p[i]] != nwestr[i + p[i]]:
					break
				else:
					p[i] = p[i] + 1
			if p[i] + i > maxright:
				maxright = p[i] + i
				maxright_i = i

			if substrlen < p[i]:
				substrlen = p[i]
				substr = i
		for i in range(substr - substrlen + 1, substr + substrlen - 1):
			if nwestr[i] != '#':
				result.append(nwestr[i])

		return (substr,substrlen,result)


								
		
solution = Solution()
a = solution.longestPalindrome('ccc')
print(a)