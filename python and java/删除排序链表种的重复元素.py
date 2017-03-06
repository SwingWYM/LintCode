class Node(object):
	def __init__(self,val,next = None):
		self.val = val
		self.next = next
	
class Link(object):
	def __init__(self):
		self.head = None

	def initList(self,data):
		if len(data) == 0:
			return
		self.head = Node(data[0])

		p = self.head

		for i in data[1:]:
			print('have')
			node = Node(i)
			p.next = node
			p = p.next
data = [0]
link = Link()
link.initList(data)

class Solution:
	def deleteDuplicatis(self,head):
		if head == None:
			return None
		s = head
		while head.next != None:
			p = head.next
			if p.val == head.val:
				head.next = p.next
			else:
				head = head.next
		print(s.val)
		return s

solution = Solution()
solution.deleteDuplicatis(link.head)
		