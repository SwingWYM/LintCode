class Solution:
	# def digitCounts(self,k,n):
	# 	sub = n // 10
	# 	rem = n % 10
	# 	i = 1
	# 	count = 0
	# 	if rem >= k:
	# 		count = sub + 1
	# 	elif sub > 0:
	# 		count = sub
	# 	print(count,rem,sub)
	# 	while sub > 0:
	# 		rem = sub % 10
	# 		sub = sub // 10
	# 		i = i * 10
	# 		if rem < k:
	# 			count = count + sub * i
	# 		elif rem == k:
	# 			count = count + sub * i + n % i + 1
	# 		else:
	# 			if k == 0:
	# 				count = count + sub * i
	# 			else:
	# 				count = count + (sub + 1) * i

	# 	return count

	def digitCounts(self,k,n):
		sub = n
		rem = 0
		i = 1
		count = 0
		while sub > 0:
			rem = sub % 10
			sub = sub // 10
			print(rem,sub)
			if rem < k:
				count = count + sub * i
			elif rem == k:
				count = count + sub * i + n % i + 1
			else:
				if k == 0:
					count = count + sub * i
				else:
					count = count + (sub + 1) * i
			print(count)
			i = i * 10
		if k == 0:
			count = count + 1
		return count

solution = Solution()
print(solution.digitCounts(1,12))
print({1:'aa'})
print({1:'aa'}[1])