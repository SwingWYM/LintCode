class Solution:
	def houseRobber(self,A):
		if len(A) == 0:
			return 0 
		if len(A) == 1:
			return A[0]
		if len(A) < 3:
			return A[0] if A[0] > A[1] else A[1]
		B = [0,A[0]]#之所以不设置B[A[0],A[1]]是因为，有可能A[0]比A[1]大，这样后面就回出错
		for i in range(2,len(A) + 1):
			B.append(max(A[i - 1] + B[i - 2],B[i - 1])) 
		return B[len(A)]
#上述方法空间为o(n)


#下面的方法空间为o(1)
class Solution:
	def houseRobber(self,A):
		if len(A) == 0:
			return 0 
		if len(A) == 1:
			return A[0]
		if len(A) < 3:
			return A[0] if A[0] > A[1] else A[1]
		B = [0,A[0]]
		for i in range(2,len(A) + 1):
			temp = B[1]
			B[1] = (max(A[i - 1] + B[0],B[1])) 
			B[0] = temp
		return B[1]


		
