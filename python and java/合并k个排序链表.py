
# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
#超时
# class Solution:
#     """
#     @param lists: a list of ListNode
#     @return: The head of one sorted list.
#     """
#     def mergeKLists(self, lists):
#         # write your code here
#         head = ListNode(0)
#         p = head
#         while len(lists) > 0:
#         	min = float('infinity')
#         	i = 0
#         	while i < len(lists):
#         		print('len:',len(lists))
#         		print('i:',i)
#         		if lists[i] is None:
#         			lists.pop(i)

#         		else:
#         			if lists[i].val < min:
#         				min = lists[i].val
#         				j = i
#         			i += 1
#         		print('j:',j)
#         		print('min:',min)
#         	if min < float('infinity'):
# 	        	lists[j] = lists[j].next
# 	        	p.next = ListNode(min)
# 	        	p = p.next
# 	        	print('s')
#         return head.next
#超时
# from functools import reduce
# class Solution:
#     def mergeKLists(self,lists):
#     	if len(lists) == 0:
#     		return None
#     	return reduce(self.merge,lists)
#     def merge(self,p,q):
#     	head = ListNode(0)
#     	s = head
#     	while p is not None and q is not None:
#     		if p.val < q.val:
#     			s.next = p
#     			p = p.next
#     		else:
#     			s.next = q
#     			q = q.next
#     		s = s.next
#     	if p is not None:
#     		s.next = p
#     	else:
#     		s.next = q
#     	return head.next



#使用归并
class Solution:
	def mergeKLists(self,lists):
		if len(lists) == 0:
			return None
		else:
			return self.partion(lists,0,len(lists) - 1)
	def partion(self,lists,start,end):
		if start < end:
			l1 = self.partion(lists,start,(start + end)//2)
			l2 = self.partion(lists,(start + end)//2 + 1,end)
			return self.merge(l1,l2)
		else:
			return lists[start]
	def merge(self,p,q):
		head = ListNode(0)
		s = head
		while p is not None and q is not None:
			if p.val < q.val:
				s.next = p
				p = p.next
			else:
				s.next = q
				q = q.next
			s = s.next
		if p is not None:
			s.next = p
		else:
			s.next = q
		return head.next
#＊＊＊＊＊＊＊＊＊＊下面这种方法可以节约一个节点，但是相对慢一些
	# def merge(self,p,q):
	# 	if p is None and q is None:
	# 		return None
	# 	if p is None:
	# 		return q
	# 	if q is None:
	# 		return p
	# 	if p.val < q.val:
	# 		temp = p
	# 		temp.next = self.merge(p.next,q)
	# 	else:
	# 		temp = q
	# 		temp.next = self.merge(p,q.next)
	# 	return temp

solution = Solution()
print(solution.mergeKLists([]))
# a = 'er'
# b = '23' + a
# print(b)