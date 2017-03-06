"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        sef.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root, the root of binary tree.
    # @return {int} The maximum amount of money you can rob tonight
    def houseRobber3(self, root):
        # write your code here
        return max(self.hoseRobber(root))

    def hoseRobber(self,root):
    	if root is None:
    		return(0,0)#返回的前面是不抢，后面是抢
    	rob_left = self.hoseRobber(root.left)
    	rob_right = self.hoseRobber(root.right)
    	not_rob =  rob_left[1] + rob_right[1] + root.val;
    	rob = max(rob_left) + max(rob_right)
    	return (not_rob,rob)