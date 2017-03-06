class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        count = 0
        r = len(grid)
        if r == 0:
        	return count
        l = len(grid[0])
        for i in range(r):
        	for j in range(l):
        		if grid[i][j] == 1:
        			count = count + 1
        			grid[i][j] = 0
        			self.DFS(grid,i,j,r,l)
        return count

    def DFS(self,grid,i,j,r,l):
    	grid[i][j] = 0
    	if i + 1 < r and grid[i + 1][j] == 1:
    		self.DFS(grid,i + 1,j,r,l)
    	if j + 1 < l and grid[i][j + 1] == 1:
    		self.DFS(grid,i,j + 1,r,l)
    	if i - 1 >= 0 and grid[i - 1][j] == 1:
    		self.DFS(grid,i - 1,j,r,l)
    	if j - 1 >= 0 and grid[i][j - 1] == 1:
    		self.DFS(grid, i, j - 1, r, l)