package Misc;

/*
 * 3034. Number of Subarrays That Match a Pattern I
 */


// brute force
class Solution {
    public int countMatchingSubarrays(int[] nums, int[] pattern) {
        int res = 0;
        int numLength = nums.length;
        int patternLength = pattern.length;
        for (int i=1; i<=numLength-patternLength+1; i++) {
            int startIndex = 0;
            int tempI = i;
            while (startIndex < patternLength && tempI < numLength) {
                int patternType = pattern[startIndex];
                if (patternType == -1 && nums[tempI] >= nums[tempI-1]) {break;}
                else if (patternType == 0 && nums[tempI] != nums[tempI-1]) {break;}
                else if (patternType == 1 && nums[tempI] <= nums[tempI-1]) {break;}
                startIndex++;
                tempI++;
            }
            if (startIndex == pattern.length) {res++;}
        }
        return res;
    }
}


// KMP Algo
