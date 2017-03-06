class ListNode(object):
	def __init__(self,val, next = None):
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


	def removeNthFromEnd(self, head, n):
		dlink = ListNode(0)
		dlink.next = head
		p = dlink
		q = dlink.next
		for i in range(n-1):
			q = q.next
		while q.next is not None:
			q = q.next
			p = p.next
		p.next = p.next.next
		return dlink.next

solution = Solution()
link = solution.initList([2,1])
dlink = solution.removeNthFromEnd(link,1)
while dlink is not None:
	print(dlink.val)
	dlink = dlink.next

