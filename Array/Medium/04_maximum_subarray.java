package Array.Medium;

/*
 * 53. Maximum Subarray
 */

class Solution {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int curr = 0;
        int currWindowSum = 0;
        while (curr < nums.length) {
            currWindowSum += nums[curr];
            res = Math.max(res, currWindowSum);
            if (currWindowSum <= 0) currWindowSum = 0;
            curr++;
        }
        return res;
    }
}