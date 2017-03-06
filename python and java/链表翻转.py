class ListNode(object):
	def __init__(self, val, next = None):
		self.val = val
		self.next = next


class Solution:

	def initList(self,data):
		link = ListNode(0)
		for i in data:
			node = ListNode(i)
			node.next = link.next
			link.next = node
			
		link = link.next
		return link

	def reverse(self, head):#head是不带头节点的链表
		rlink = ListNode(0)
		while head is not None:
			node = ListNode(head.val)
			node.next = rlink.next
			rlink.next = node
			head = head.next
		rlink = rlink.next
		return rlink


solution = Solution()
link = solution.initList([1,2,3])
rlink = solution.reverse(link)
while rlink is not None:
	print(rlink.val)
	rlink = rlink.next
