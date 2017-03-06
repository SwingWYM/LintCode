"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        p = ListNode(0)
        q = ListNode(0)
        ptr = head
        head = p
        mid = q
        while ptr is not None:
            if ptr.val < x:
                p.next = ptr
                p = p.next
            else:
                q.next = ptr
                q = q.next
            ptr = ptr.next
        p.next = mid.next
        q.next = None
        return head.next