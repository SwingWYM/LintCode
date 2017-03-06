class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
class Solution:
	def inter(self,A):
		if len(A) == 0:
			return
		n = len(A)//2
		node = TreeNode(A[n])
		node.left = self.inter(A[:n])
		node.right = self.inter(A[n+1:])
		return node

	def sortedArrayToBST(self,A):
		if len(A) > 0:
			n = len(A)//2
			tree = TreeNode(A[n])
			tree.left = self.inter(A[:n])
			tree.right = self.inter(A[n+1:])
			return tree
		else:
			return None

solution = Solution()
result = solution.sortedArrayToBST([1,2,3,4,6,8,9])
node = result
while node is not None:
	print(node.val)
	node = node.left
