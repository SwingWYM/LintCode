#快排的思想，每一轮过后，下次都只再排另一边。
class Solution:
	def kthLargestElement(self,k,A):
		result = self.quickSort(A,0,len(A) - 1,k)
		return result

	def quickSort(self,A,low,high,k):
		if low > high:
			return
		key = A[low]
		p = low
		q = high
		while p < q:
			while A[q] <= key and p < q:
				q = q - 1
			A[p] = A[q]
			while A[p] >= key and p < q:
				p = p + 1
			A[q] = A[p]
		A[p] = key
		if p > k - 1:
			return self.quickSort(A,low,p - 1,k)
		elif p == k - 1:
			return A[p]
		else:
			return self.quickSort(A,p + 1,high,k)

solution = Solution()
print(solution.kthLargestElement(10,[1,2,3,4,5,6,8,9,7,10]))