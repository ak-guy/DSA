package Misc;

/*
 * 2305. Fair Distribution of Cookies
 */
class Solution {
    private int res = Integer.MAX_VALUE;

    private void rec(int startingIndex, int[] cookies, int k, int[] possibleDistribution, int cookiesLen) {
        if (startingIndex == cookiesLen) {
            int maxVal = 0;
            for (int val: possibleDistribution) {
                maxVal = Math.max(maxVal, val);
            }
            res = Math.min(res, maxVal);
            return;
        }

        for (int ind=0; ind<k; ind++) {
            if (possibleDistribution[ind] + cookies[startingIndex] < res){
                possibleDistribution[ind] += cookies[startingIndex];
                rec(startingIndex+1, cookies, k, possibleDistribution, cookiesLen);
                possibleDistribution[ind] -= cookies[startingIndex];
            } 
        }
    }

    public int distributeCookies(int[] cookies, int k) {
        int cookiesLen = cookies.length;
        rec(0, cookies, k, new int[k], cookiesLen);
        return res;
    }
}
