class ListNode(object):
	def __init__(self,val,next=None):
		self.val = val
		self.next = next

class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class Solution:

	def initList(self,A):
		List = ListNode(0)
		p = List
		for i in A:
			node = ListNode(i)
			p.next = node
			p = p.next
		return List.next

	def inter(self,head,num):
		if num != 0 and head is not None:
			n = num//2
			node = head
			for i in range(n):
				node = node.next
			treeNode = TreeNode(node.val)
			# print(treeNode.val)
			treeNode.right = self.inter(node.next,num-(n+1))
			node = None
			treeNode.left = self.inter(head,n)
			# print(treeNode.val)
			return treeNode
		else:
			return
		                                                                                              

	def sortedListToBST(self,head):
		if head is not None:
			node = head
			num = 0
			while node is not None:
				num = num + 1
				node = node.next
			# print(i)
			n = num//2
			node = head
			for i in range(n):
				node = node.next
			# print(node.val)
			tree = TreeNode(node.val)
			tree.right = self.inter(node.next,num-(n+1))
			node = None
			tree.left = self.inter(head,n)
			# print(head.val)
			return tree
		else:
			return None
		



solution = Solution()
head = solution.initList([1,2,3,4,5,6])
# while head is not None:
# 	print (head.val)
# 	head = head.next
result = solution.sortedListToBST(head)
p = result
while p is not None:
	# print(p.val)
	p = p.left
q = result
while q is not None:
	# print(q.val)
	q = q.right