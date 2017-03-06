"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        node = ListNode(0)
        node.next = head
        head = node
        p = head
        s = head.next
        q = head.next.next
        i = 1
        while i < m:
            p = p.next
            q = q.next
            i += 1
        while i < n:
            s.next = q.next
            q.next = p.next
            p.next = q
            q = s.next
            i = i += 1
        return head.next