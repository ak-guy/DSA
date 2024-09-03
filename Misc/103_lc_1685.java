package Misc;

/*
 * 1685. Sum of Absolute Differences in a Sorted Array
 */

 class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        int n = nums.length;
        int[] prefixSum = new int[n];
        int[] suffixSum = new int[n];

        // build prefixSum
        prefixSum[0] = nums[0];
        for(int i=1; i<n; i++){
            prefixSum[i] = nums[i] + prefixSum[i-1];
        }

        // build suffixSum
        suffixSum[n-1] = nums[n-1];
        for (int i=n-2; i>=0; i--) {
            suffixSum[i] = nums[i] + suffixSum[i+1];
        }

        int[] res = new int[n];
        for (int i=0; i<n; i++) {
            int prev = i==0 ? 0 : (nums[i] * (i)) - prefixSum[i-1];
            int next = i==n-1 ? 0 : suffixSum[i+1] - (nums[i] * (n-i-1));
            res[i] = prev + next;
        }

        return res;
    }
}