package Misc;

import java.util.*;

/*
 * 3286. Find a Safe Walk Through a Grid
 */
class Solution {
    private boolean getRes(int r, int c, int health, int[][][] dp, int[][] visited, int n, int m, List<List<Integer>> grid) {
        if (r<0 || r==n || c<0 || c==m || health<0 || visited[r][c] == 1) {
            return false;
        }
        if (r==n-1 && c==m-1) {
            if (health>grid.get(r).get(c)) {
                return true;
            }
            return false;
        }

        if (dp[r][c][health] != -1){
            boolean toReturn = dp[r][c][health]==0 ? false: true;
            return toReturn;
        }

        visited[r][c] = 1;
        int newHealth = health-grid.get(r).get(c);
        boolean up = getRes(r-1,c,newHealth, dp,visited,n,m,grid);
        boolean down = getRes(r+1,c,newHealth, dp,visited,n,m,grid);
        boolean left = getRes(r,c-1,newHealth, dp,visited,n,m,grid);
        boolean right = getRes(r,c+1,newHealth, dp,visited,n,m,grid);
        visited[r][c] = 0;
        dp[r][c][health] = up || down || left || right ? 1 : 0;
        return dp[r][c][health] == 1;
    }

    public boolean findSafeWalk(List<List<Integer>> grid, int health) {
        int n = grid.size();
        int m = grid.get(0).size();
        int[][][] dp = new int[health+1][n][m];
        for (int[][] i: dp) {
            for (int[] j: i) {
                Arrays.fill(j, -1);
            }
        }
        int[][] visited = new int[n][m];
        
        return getRes(0,0,health,dp,visited,n,m,grid);
    }
}
