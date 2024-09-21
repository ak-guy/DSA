package Array.Hard;

/*
 * 152. Maximum Product Subarray
 */

class Solution {
    public int maxProduct(int[] nums) {
        // logic is simple just take max of forwardRunningProduct and backwardRunningProduct
        int n = nums.length;
        int forwardRunningProduct = 1;
        int backwardRunningProduct = 1;
        int res = nums[0];
        for (int i=0; i<n; i++) {
            // we are using ternary operator because we need to reset the productCounter if it becomes 0
            forwardRunningProduct = (forwardRunningProduct == 0 ? 1 : forwardRunningProduct) * nums[i];
            backwardRunningProduct = (backwardRunningProduct == 0 ? 1 : backwardRunningProduct) * nums[n-i-1];
            res = Math.max(res, Math.max(forwardRunningProduct, backwardRunningProduct));
        }
        return res;
    }
}