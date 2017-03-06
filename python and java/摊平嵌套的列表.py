# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """




#nestedList->[[xxxxxx]]，里面的xxx都是NestedInteger对象
class NestedIterator(object):

    def __init__(self, nestedList):

        # Initialize your data structure here.
        self.s = []
        for i in range(0,len(nestedList))[::-1]:
        	self.s.append(nestedList[i])
        
    # @return {int} the next element in the iteration
    def next(self):
    	t = self.s.pop()
    	if t.isInteger():
    		return t.getInteger()
        # Write your code here
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
    	while self.s:
	    	t = self.s[-1]
	    	if t.isInteger():
	    		return True
	    	else:
	    		self.s.pop()
	    		for i in range(0,len(t.getList()))[::-1]:
	    			self.s.append(t.getList()[i])
# Your NestedIterator object will be instantiated and called as such:
# nestedList = [1,2]
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

