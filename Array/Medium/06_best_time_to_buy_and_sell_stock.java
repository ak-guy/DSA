package Array.Medium;

/*
 * 121. Best Time to Buy and Sell Stock
 */

class Solution {
    public int maxProfit(int[] prices) {
        /*
        Idea is to consider buying at every index if it is cheaper than before
        and if that is not the case then we can consider selling the stock there
         */
        int prevBoughtAt = Integer.MAX_VALUE;
        int prevSellAt = 0;
        int res = 0;
        for (int i=0; i<prices.length; i++) {
            if (prevBoughtAt > prices[i]) prevBoughtAt = prices[i];
            else {
                prevSellAt = prices[i];
                res = Math.max(res, prevSellAt-prevBoughtAt);
            }
        }
        return res;
    }
}