package Misc;

/*
 * 2304. Minimum Path Cost in a Grid
 */
import java.util.*;
class Solution {
    private int getMinPath(int row, int col, int[][] grid, int[][] moveCost, int totalCols, int[][] dp) {
        if (row==grid.length-1) {
            return grid[row][col];
        };

        if (dp[row][col]!=-1) {return dp[row][col];}

        int res = Integer.MAX_VALUE;
        for (int i=0; i<totalCols; i++) {
            res = Math.min(res, grid[row][col] + moveCost[grid[row][col]][i] + getMinPath(row+1, i, grid, moveCost, totalCols, dp));
        }
        dp[row][col]=res;
        return dp[row][col];
    }

    public int minPathCost(int[][] grid, int[][] moveCost) {
        int res = Integer.MAX_VALUE;
        int col = 0;
        int totalCols = grid[0].length;
        int[][] dp = new int[51][51];
        for(int[] row: dp) {
            Arrays.fill(row, -1);
        }
        for (int i=0; i<totalCols; i++) {
            int possibleRes = getMinPath(0, col, grid, moveCost, totalCols, dp);
            res = Math.min(res, possibleRes);
            col++;
        }

        return res;
    }
}