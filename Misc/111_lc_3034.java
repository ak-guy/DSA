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
class KMP {
    private int[] computeLPS(int[] pattern) {
        int n = pattern.length;
        int[] lps = new int[n]; // longest prefix suffix

        int currInd = 1;
        int maxMatchingChars = 0;
        while (currInd < n) {
            if (pattern[currInd] == pattern[maxMatchingChars]) {
                lps[currInd]=maxMatchingChars+1;
                currInd++;
                maxMatchingChars++;
            }else {
                if (maxMatchingChars == 0) {
                    lps[currInd] = 0;
                    currInd++;
                }else {
                    maxMatchingChars = lps[maxMatchingChars-1];
                }
            }
        }
        return lps;
    }

    private int getResultCount(int[] text, int[] pattern) {
        int res = 0;
        int[] lps = computeLPS(pattern);

        int patternInd = 0;
        int textInd = 0;
        while (textInd < text.length) {
            if (pattern[patternInd] == text[textInd]) {
                patternInd++;
                textInd++;
            }else {
                if (patternInd == 0) {
                    textInd++;
                }else {
                    patternInd = lps[patternInd-1];
                }
            }
            if (patternInd == pattern.length) {
                res++;
                patternInd = lps[patternInd-1];
            }
        }
        return res;
    }

    public int countMatchingSubarrays(int[] nums, int[] pattern) {
        int numsLength = nums.length;
        int[] text = new int[numsLength-1];
        for (int i=1; i<numsLength; i++) {
            if (nums[i] > nums[i-1]) {text[i-1]=1;}
            else if (nums[i] == nums[i-1]) {text[i-1]=0;}
            else {text[i-1]=-1;}
        }

        return getResultCount(text, pattern);
    }
}