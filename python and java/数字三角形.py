class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if len(triangle) == 1 and len(triangle[0]) == 1:
        	return triangle[0][0]
        if len(triangle) == 1 and len(triangle[0]) == 0:
        	return None
        if len(triangle) == 0:
        	return None
        for i in range(1,len(triangle)):
        	for j in range(0,len(triangle[i])):
        		#为了防止越界
        		triangle[i][j] = triangle[i][j] + min(triangle[i - 1][max(j - 1,0)],triangle[i - 1][min(j,i - 1)])
        s = triangle[-1][0]
        for i in triangle[-1]:
        	if i < s:
        		s = i
        return s



#上面的空间复杂度是否是1，因为是在原数组上进行的，如果要体现出o(n)，可以用一个新数组来存
#每次只需要存一行，不需要每一行都存
class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if len(triangle) == 1 and len(triangle[0]) == 1:
        	return triangle[0][0]
        if len(triangle) == 1 and len(triangle[0]) == 0:
        	return None
        if len(triangle) == 0:
        	return None
        buff = [triangle[0][0]]
        for i in range(1,len(triangle)):
        	for j in range(0,len(triangle[i]))[::-1]:#从后往前
        		if j < len(triangle[i]) - 1:
        			buff[j] = triangle[i][j] + min(buff[min(j,i - 1)],buff[max(j - 1,0)])
        		else:
        			buff.append(triangle[i][j] + min(buff[min(j,i - 1)],buff[max(j - 1,0)]))
        s = buff[0]
        for i in buff:
        	if i < s:
        		s = i
        return s



