class Solution:
	def houseRobber2(self,A):
		if len(A) == 0:
			return 0 
		if len(A) == 1:
			return A[0]
		if len(A) < 3:
			return A[0] if A[0] > A[1] else A[1]
		B = A[1:]
		C = A[:len(A) - 1]
		return max(self.houseRobber(B),self.houseRobber(C))

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

#上述方法空间为o(n)


#下面的方法空间为o(1)
class Solution:
	def houseRobber2(self,A):
		if len(A) == 0:
			return 0 
		if len(A) == 1:
			return A[0]
		if len(A) < 3:
			return A[0] if A[0] > A[1] else A[1]
		B = [A[0],A[1]]
		for i in range(2,len(A)):
			temp = B[1]
			B[1] = (max(A[i] + B[0],B[1])) 
			B[0] = temp
		return B[1]