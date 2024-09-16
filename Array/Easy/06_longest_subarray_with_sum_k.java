package Array.Easy;

import java.util.*;
/*
 * Longest Sub-Array with Sum K -> https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
 */
class Solution {
    // sequel to subarry sum eqauls k (LC one)
    public static int lenOfLongSubarr(int nums[], int N, int k) {
        int runningSum = 0;
        Map<Integer, Integer> sumVsFirstIndex = new HashMap<>();
        sumVsFirstIndex.put(0,-1);
        int res = 0;
        
        for (int i=0; i<nums.length; i++) {
            runningSum += nums[i];
            int diff = runningSum - k;
            res = Math.max(res, i-sumVsFirstIndex.getOrDefault(diff,i));
            sumVsFirstIndex.putIfAbsent(runningSum, i);
        }

        return res;
    }
}