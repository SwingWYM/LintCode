public class Solution{
	public ListNode sortList(ListNode head){
		quickSort(head,null);
		return head; 
	}

	public void quickSort(ListNode head,ListNode end){
		if (head != end) {
			ListNode low = head;
			ListNode high = head.next;
			int key = head.val;
			int temp;
			while(high != end){
				if (high.val < key) {
					low = low.next;
					temp = low.val;
					low.val = high.val;
					high.val = temp;
				}
				high = high.next;
			}
			temp = low.val;
			low.val = key;
			head.val = temp;
			quickSort(head,low);
			quickSort(low.next,end);
		}
	}

	public ListNode mergeSort(ListNode head){
		ListNode left,right,L1,L2;
		if (head == null || head.next == null) {
			return head;
		}
		left = head;
		right = split(head);
		L1 = mergeSort(left);
		L2 = mergeSort(right);
		return merge(L1,L2);
	}

	public ListNode merge(ListNode left,ListNode right){
		ListNode p,q;
		p = ListNode(0);
		while (left != null && right!= null) {
			if (left.val < right.val) {
				p.next = left;
				p = p.next;
				left = left.next;
			}
			else{
				p.next = right;
				right = right.next;
				p = p.next;
			}
		}
		if (left != null) {
			p.next = left;
		}
		else if (right != null) {
			p.next = right;
		}
		else{
			p.next = null;
		}
		return q;
	}

	public ListNode split(ListNode head){
		ListNode slow,fast,prev;
		slow = head;
		fast = head;
		prev = head;
		while(fast && fast.next){
			prev = slow;
			slow = slow.next;
			fast = fast.next.next;
		}
		prev.next = null;
		return slow;
	}
}