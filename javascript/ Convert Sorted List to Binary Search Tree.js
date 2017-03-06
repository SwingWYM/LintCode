function ListNode(val){
	this.val = val;
	this.next = null;
}
function TreeNode(val){
	this.val = val;
	this.left = this.right = null;
}

var initList = function(A){
	var list = new ListNode(0);
	var p = list;
	for (prop in A) {
		if (A.hasOwnProperty(prop)) {
			var node = new ListNode(A[prop]);
			// debug(node.val)
			p.next = node;
			p = p.next;
		}
	}
	return list.next;
}

var sortedListToBST = function(head){
	if (head !== null) {
		var node = head;
		var pre = head;
		var num = 0;
		while (node !== null) {
			num = num + 1;
			node = node.next;
		}
		var n = Math.floor(num/2);
		node = head;
		for (var i = 0; i < n; i++) {
			pre = node;
			node = node.next;
		}
		tree = new TreeNode(node.val);
		pre.next = null;
		debug(pre.val)
		tree.right = inter(node.next,num-(n+1));
		tree.left = inter(head,n);
		
		return tree;
	}
	else{
		return null;
	}
}

var inter = function(head,num){
	if (num !== 0 && head !== null) {
		var n = Math.floor(num/2);
		var pre = head;
		var node = head;
		for (var i = 0; i < n; i++) {
			pre = node;
			node = node.next;
		}
		var treeNode = new TreeNode(node.val);
		// debug(treeNode.val)
		treeNode.right = inter(node.next,num-(n+1));
		pre.next = null;
		treeNode.left = inter(head,n);

		// debug(treeNode.val)
		return treeNode;
	}
	else{
		return null;
	}
}

// function sortedListToBST(head) {
//     if (!head) {
//         return null;
//     }
    
//     if (!head.next) {
//         return new TreeNode(head.val);
//     }
    
//     var m = head;
//     var prev = head;
//     var tail = head;
    
//     // head, prev, m -> ... -> null
//     while (tail && tail.next) {
//         tail = tail.next.next;
//         prev = m;
//         m = m.next;
//     }
//     // head -> ... -> prev -> m -> ... -> null
    
//     prev.next = null;
    
//     var n = new TreeNode(m.val);
//     n.left = sortedListToBST(head);
//     n.right = sortedListToBST(m.next);
//     return n;
// }

head = initList([1,2,3,4,5,6]);
// while (head != null) {
// 	debug(head.val);
// 	head = head.next;
// }
result = sortedListToBST(head);
p = result;
while (p != null) {
	debug(p.val);
	p = p.left;
}
q = result;
while (q != null) {
	debug(q.val);
	q = q.right;
}
