package Array.Easy;

/*
 * 189. Rotate Array
 */

class Solution {
    private void reverse(int start, int end, int[] nums) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
    
    public void rotate(int[] nums, int k) {
        int numsLen = nums.length;
        k %= numsLen;
        if (k==0) return;
        
        // reverse whole array
        reverse(0, numsLen-1, nums);

        // reverse first k
        reverse(0, k-1, nums);

        // then reverse k till last index
        reverse(k, numsLen-1, nums);
    }
}