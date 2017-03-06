class ListNode(ojbect):
	def __init__(self,val,next = None):
		self.val = val
		self.next = next

#quik sort
class Solution:
	def sortList(self,head):
		# end = None
# 		while end is not None:
# 			end = end.next
		self.quikSort(head,None)
		return head
		#因为链表断开了，所以需要将重新拼接的链表返回，而不再是直接取头节点
		head = self.mergSort(head)
		return head
	#快排：位置交换
	# 这种是值交换的方法,链表不需要截断。因为先比较大范围，再比较小范围，没有合并过程
	def quikSort(self,head,end):
		if head != end:
			p = head.val
			low = head
			high = head.next
			while high is not end:
				if high.val < p:
					low = low.next
					temp = low.val
					low.val = high.val
					high.val = temp
				high = high.next
			temp = low.val
			low.val = p
			head.val = temp
			self.quikSort(head,low)
			self.quikSort(low.next,end)


	#两边都有序的情况下
	#链表截断较方便，因为从小范围开始比较，后面有合并的过程。
def mergSort(self,head):
		if not head or not head.next:
			return head
		left,right = self.split(head)
		L1 = self.mergSort(left)
		L2 = self.mergSort(right)
		return self.merge(L1,L2)

	def merge(self,left,right):
	   # print(left is None)
	   # print(right)
	   # if left is None:
	   #     return right
	   # if right is None:
	   #     return left
		p = ListNode(0)
		head = p
		while left and right:
			if left.val < right.val:
				head.next = left
				left = left.next
				head = head.next
			else:
				head.next = right
				right = right.next
				head = head.next
		if left:
			head.next = left
		elif right:
			head.next = right
		else:
		    head.next = None
		return p.next
		
	def split(self,head):
		slow = head
		fast = head
		prev = head
# 		print(fast)
		while fast and fast.next:
			prev = slow
			slow = slow.next
			fast = fast.next.next
		prev.next = None
		return head,slow


	#这种是指针交换的方法：指针交换慢很多
	def quikSort(self,head,end):
		if head == end or head.next == end:
			return
		key = head
		low = head
		high = head
		t = head.next
		while t != end:
			if t.val < key:
				low.next = t
				low = low.next
			else:
				high.next = t
				high = high.next
		low.next = key
		high.next = end
		self.quikSort(head,key)
		self.quikSort(key.next,end)
