package Array.Easy;

/*
 * 485. Max Consecutive Ones
 */

class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int start = 0;
        int end = 0;
        int numsLen = nums.length;
        int res = 0;
        while (end < numsLen) {
            while (end < numsLen && nums[end] == 1) {
                end++;
            }
            res = Math.max(res, end-start);
            end++;
            start=end;
        }
        return res;
    }
}
