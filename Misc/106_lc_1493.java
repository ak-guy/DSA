package Misc;

/*
 * 1493. Longest Subarray of 1's After Deleting One Element
 */

class Solution {
    public int longestSubarray(int[] nums) {
        int slidingWindowStartIndex = 0;
        int slidingWindowEndIndex = 0;

        boolean zeroEncountered = false;
        int res = 0;
        int currentMax = 0;

        while (slidingWindowEndIndex < nums.length) {
            if(nums[slidingWindowEndIndex] == 0 && zeroEncountered == false) {zeroEncountered = true;}
            else if (nums[slidingWindowEndIndex] == 0 && zeroEncountered == true) {
                while (nums[slidingWindowStartIndex] != 0) {
                    slidingWindowStartIndex++;
                    currentMax--;
                }
                slidingWindowStartIndex++;
            }else {currentMax++;}
            // System.out.println("startIndex=" + slidingWindowStartIndex + " ,endIndex=" + slidingWindowEndIndex);
            res = Math.max(res, currentMax);
            slidingWindowEndIndex++;
        }

        if (slidingWindowStartIndex == 0) {return nums.length-1;}
        return res;
    }
}