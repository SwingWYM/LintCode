class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None
		
class Link(object):
	def __init__(self):
		self.head = None
	def initlist(self,data):
		if len(data) == 0:
			return
		self.head = Node(data[0])
		p = self.head
		for i in data[1:]:
			p.next = Node(i)
			p = p.next

data1 = [1,1,1,1]
data2 = [9,8,8,8]
link1 = Link()
link1.initlist(data1)
link2 = Link()
link2.initlist(data2)

class Solution:
	def addLists(self, l1, l2):
		if l1 == None:
			return l2
		if l2 == None:
			return l1
		p = Node(0)
		p.next = l1
		q = Node(0)
		q.next = l2
		m = 0
		while (p.next is not None) and (q.next is not None):
			sum = p.next.val + q.next.val + m
			if sum > 9:
				p.next.val = sum % 10
				m = sum // 10
			else:
				p.next.val = sum
				m = 0
			p = p.next
			q = q.next
		if p.next is not None:
			p.next.val = p.next.val + m
			m = 0
		if q.next is not None:
			q.next.val = q.next.val + m
			p.next = q.next
			m = 0
		if m != 0:
			p.next = Node(m)
		return l1
		
solution = Solution()
s = solution.addLists(link1.head,link2.head)
while s is not None:
	print(s.val)
	s = s.next