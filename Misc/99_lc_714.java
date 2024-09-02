package Misc;

/*
 * 714. Best Time to Buy and Sell Stock with Transaction Fee
 */

import java.util.*;

class Solution {
    private int helper(int startingIndex, int isBought, int[] prices, int fee, int[][] dp, int pricesLength) {
        if (startingIndex == pricesLength) {
            return 0;
        }

        if (dp[startingIndex][isBought] != -1) {
            return dp[startingIndex][isBought];
        }
        
        int profit = 0;
        if (isBought == 0) {
            profit = Math.max(helper(startingIndex+1, 0, prices, fee, dp, pricesLength), helper(startingIndex+1, 1, prices, fee, dp, pricesLength) - prices[startingIndex]);
        }else {
            profit = Math.max(helper(startingIndex+1, 1, prices, fee, dp, pricesLength), helper(startingIndex+1, 0, prices, fee, dp, pricesLength) + prices[startingIndex] - fee);
        }

        dp[startingIndex][isBought] = profit;
        return dp[startingIndex][isBought];
    }

    public int maxProfit(int[] prices, int fee) {
        int pricesLength = prices.length;
        int[][] dp = new int[pricesLength][2];

        for (int[] row: dp) {
            Arrays.fill(row, -1);
        }

        int res = helper(0, 0, prices, fee, dp, pricesLength);
        return res;
    }
}
