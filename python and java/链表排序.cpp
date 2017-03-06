class Solution{
public:
	ListNode *sortList(ListNode *head){
		quickSort(head,NULL);
		return head;
	}

	ListNode *quickSort(ListNode *head,ListNode *end){
		if (head != end)
		{
			ListNode *low = head;
			ListNode *high = head->next;
			int key = head->val;
			int temp;
			while(high != end){
				if (high->val < key)
				{
					low = low->next;
					temp = low->val;
					low->val = high->val;
					high->val = temp;
				}
				high = high->next;
			}
			temp = low->val;
			low->val = key;
			head->val = temp;
			quickSort(head,low);
			quickSort(low->next,end);
		}
		
	}
};