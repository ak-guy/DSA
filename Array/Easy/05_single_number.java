package Array.Easy;

/*
 * 136. Single Number
 */

class Solution {
    public int singleNumber(int[] nums) {
        int prev = nums[0];
        int res=prev;
        for (int i=1; i<nums.length; i++) {
            int curr = nums[i];
            res = curr ^ prev;
            prev = res;
        }
        return res;
    }
}