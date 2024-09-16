package Array.Easy;

/*
 * 283. Move Zeroes
 */

class Solution {
    public void moveZeroes(int[] nums) {
        int numsLen = nums.length;
        int first = 0;
        int second = 1;
        while (second < numsLen) {
            if (nums[first] == 0) {
                while (second < numsLen && nums[second] == 0) {
                    second++;
                }
                if (second >= numsLen) break;
                int temp = nums[first];
                nums[first] = nums[second];
                nums[second] = temp;
            }
            first++;
            second++;
        }
    }
}