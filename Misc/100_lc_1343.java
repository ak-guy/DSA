package Misc;

/*
 * 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
 */

 class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        double currentAverage = 0;
        int currentSum = 0;
        for (int i=0; i<k; i++) {
            currentSum += arr[i];
        }

        currentAverage = currentSum / k;
        int startSWIndex = 1;
        int endSWIndex = k;
        int res = 0;
        if (currentAverage >= threshold) {res++;}

        while (endSWIndex < arr.length) {
            currentAverage = currentAverage + (((double) arr[endSWIndex] - (double) arr[startSWIndex-1]) / k);
            if (currentAverage >= threshold) {
                res++;
            }
            endSWIndex++;
            startSWIndex++;
        }
        return res;
    }
}