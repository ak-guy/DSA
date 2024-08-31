package Misc;
/*
 * 1020. Number of Enclaves
 */

 class Solution {
    private void expandSea(int r, int c, int[][] grid) {
        grid[r][c] = 0;
        int[][] directions = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        for (int[] direction: directions) {
            int row = direction[0] + r;
            int col = direction[1] + c;
            if (row>=0 && row<grid.length && col>=0 && col<grid[0].length && grid[row][col] == 1){
                expandSea(row, col, grid);
            }
        }
    }

    public int numEnclaves(int[][] grid) {
        int res = 0;
        int n = grid.length;
        int m = grid[0].length;

        // traversing boundary cell and making all adjacent cells of 1 zero
        for (int r=0; r<n; r++) {
            if (r==0 || r==n-1) {
                for (int c=0; c<m; c++) {
                    if (grid[r][c]==1) {expandSea(r,c,grid);}
                }
            }else {
                if (grid[r][0] == 1) {expandSea(r,0,grid);}
                if (grid[r][m-1] == 1) {expandSea(r,m-1,grid);}
            }
        }
        
        // traversing inner cells and finding all walkable cells
        for (int r=1; r<n-1; r++) {
            for (int c=1; c<m-1; c++) {
                if (grid[r][c]==1) {
                    res += 1;
                }
            }
        }
        return res;
    }
}

public class 94_lc_1020 {
    
}
