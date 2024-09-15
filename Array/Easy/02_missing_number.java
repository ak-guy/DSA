package Array.Easy;

/*
 * 268. Missing Number
 */

class Solution {
    public int missingNumber(int[] nums) {
        int numsLen = nums.length;
        for (int i=0; i<numsLen; i++) {
            int curr = Math.abs(nums[i]);

            if (curr == numsLen) {
                continue;
            }

            if (curr == Integer.MAX_VALUE || curr == 0) {
                nums[0] = nums[0] == 0 ? Integer.MAX_VALUE : -1 * nums[0];
            }else {
                if (nums[curr] == 0) nums[curr] = Integer.MAX_VALUE;
                else nums[curr] = -1 * nums[curr];
            }
        }
        
        for (int i=0; i<numsLen; i++) {
            if (nums[i] >= 0 && nums[i] != Integer.MAX_VALUE) return i;
        }
        return numsLen;

    }
}