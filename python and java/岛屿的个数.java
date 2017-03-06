public class Solution {
    /**
     * @param grid a boolean 2D matrix
     * @return an integer
     */
    public int numIslands(boolean[][] grid) {
        // Write your code here
        int r = grid.length;
        int count = 0;
        int l;
        if (r == 0) {
        	return count;
        }
        l = grid[0].length;
        for (int i = 0; i < r; i++) {
        	for (int j = 0; j < l; j++) {
        		if (grid[i][j] == true) {
        			count++;
        			grid[i][j] = false;
        			DFS(grid, i, j, r, l);
        		}
        	}
        }
        return count;
    }

    public void DFS(boolean[][] grid,int i, int j, int r, int l){
    	grid[i][j] = false;
    	if (i + 1 < r && grid[i + 1][j] == true) {
    		DFS(grid, i + 1, j, r, l);
    	}
    	if (j + 1 < l && grid[i][j + 1] == true) {
    		DFS(grid, i, j + 1, r, l);
    	}
    	if (i - 1 >= 0 && grid[i - 1][j] == true) {
    		DFS(grid, i - 1, j, r, l);
    	}
    	if (j - 1 >= 0 && grid[i][j - 1] == true) {
    		DFS(grid, i, j - 1, r, l);
    	}
    }
}