package Misc;

/*
 * 1029. Two City Scheduling
 */

 // brute force
class Solution {
    private int rec(int start, int cityA, int cityB, int[][] costs, int res) {
        if (start == costs.length-1) return cityA == 1 ? costs[start][0] : costs[start][1];

        int takeCityA = Integer.MAX_VALUE;
        if (cityA>0) takeCityA = costs[start][0] + rec(start+1, cityA-1, cityB, costs, res+costs[start][0]);
        
        int takeCityB = Integer.MAX_VALUE;
        if (cityB>0) takeCityB = costs[start][1] + rec(start+1, cityA, cityB-1, costs, res+costs[start][1]);
        return Math.min(takeCityA, takeCityB);
    }

    public int twoCitySchedCost(int[][] costs) {
        int costsLen = costs.length;
        int res = rec(0, costsLen/2, costsLen/2, costs, 0);
        return res;
    }
}

// optimized Greedy + sort
