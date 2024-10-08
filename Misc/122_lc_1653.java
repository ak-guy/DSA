// package Misc;

/* 
 * 1653. Minimum Deletions to Make String Balanced
 * Help -> https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/solutions/943968/java-dp-accepted-explanation/
 */


// to Review (Not correct solution)
class Memoization {
    private int memoize(int ind, int bCount, String s, int[] dp) {
        if (ind == s.length()) return 0;

        int minDeletion;
        if (s.charAt(ind) == 'a') {
            // option 1: delete all b that occured before ind
            // option 2: delete current a
            minDeletion = Math.min(bCount, 1 + memoize(ind+1, bCount, s, dp));
        }else {
            minDeletion = memoize(ind+1, bCount+1, s, dp);
        }

        dp[ind] = minDeletion;
        return dp[ind];
    }

    public int minimumDeletions(String s) {
        int sLen = s.length();
        int[] dp = new int[sLen+1];
        memoize(0, 0, s, dp);
        return dp[sLen];
    }
}


// correct solution
class Solution {
    public int minimumDeletions(String s) {
        int sLen = s.length();
        int bCount = 0;
        int[] dp = new int[sLen+1]; // (1-based index) it will store what number of deletions we need to make till that index

        for (int i=0; i<sLen; i++) {
            if (s.charAt(i) == 'a') {
                // two cases while handling 'a', either delete all 'b' occured before it or delete current 'a', so deleting current 'a' will result in total dp[i] + 1 deletions
                dp[i+1] = Math.min(bCount, dp[i]+1);
            }else {
                dp[i+1] = dp[i]; // in case we get 'b', we are setting minimum deletion value as prev value in dp, because according to problem we dont to consider deleting it 
                bCount++;
            }
        }
        return dp[sLen];
    }
}