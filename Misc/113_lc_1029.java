package Misc;

/*
 * 1029. Two City Scheduling
 */

import java.util.*;

// brute force
class Solution {
    private int rec(int start, int cityA, int cityB, int[][] costs, int[][][] dp) {
        if (start == costs.length-1) return cityA == 1 ? costs[start][0] : costs[start][1];
        
        if (dp[start][cityA][cityB] != -1) return dp[start][cityA][cityB];
        
        int takeCityA = Integer.MAX_VALUE;
        if (cityA>0) takeCityA = costs[start][0] + rec(start+1, cityA-1, cityB, costs, dp);
        
        int takeCityB = Integer.MAX_VALUE;
        if (cityB>0) takeCityB = costs[start][1] + rec(start+1, cityA, cityB-1, costs, dp);

        return dp[start][cityA][cityB] = Math.min(takeCityA, takeCityB);
    }

    public int twoCitySchedCost(int[][] costs) {
        int costsLen = costs.length;
        int[][][] dp = new int[costsLen+1][costsLen/2+1][costsLen/2+1];
        for (int[][] r: dp) {
            for (int[] c: r) {
                Arrays.fill(c, -1);
            }
        }
        int res = rec(0, costsLen/2, costsLen/2, costs, dp);
        return res;
    }
}

// optimized Greedy + sort
class Optimized {
    /* 
     * so the problem statement is we need to send half people to cityA and half to cityB
     * what we can do is send all people to cityA and then later choose which half people we 
     * need to send to cityB, based on diff bw cityB-cityA
     * Now suppose difference is -ve that would mean if we had sent the cityB here instead of 
     * cityA we would have saved some cost. So get the diff array and pick smallest half, that
     * is the max amount we could save if we had choose to sent these guys to cityB instead of cityA
     */
    public int twoCitySchedCost(int[][] costs) {
        int totalCityA = 0;
        int n = costs.length;
        int[] diffArray = new int[n];
        int ind=0;
        for (int[] city: costs) {
            totalCityA += city[0];
            diffArray[ind] = city[1]-city[0];
            ind++;
        }
        Arrays.sort(diffArray);
        for (int i=0; i<n/2; i++) {
            totalCityA += diffArray[i];
        }

        return totalCityA;
    }
}