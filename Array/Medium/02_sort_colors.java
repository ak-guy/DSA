package Array.Medium;

/*
 * 75. Sort Colors
 */

class Solution {
    public void sortColors(int[] nums) {
        /*
        The idea behind the algorithm is to keep all the 0s before the low pointer,
        all the 2s after the high pointer, and all the 1s between the low and high 
        pointers. The algorithm moves the mid pointer through the array, comparing 
        the value at each position with 1. If the value is 0, the element is swapped
        with the element at the low pointer, and the low and mid pointers are 
        incremented. If the value is 2, the element is swapped with the element at
        the high pointer, and the high pointer is decremented. If the value is 1, 
        the mid pointer is simply incremented.
        */
        int start = 0;
        int end = nums.length-1;
        int curr = 0;
        while (curr <= end) {
            if (nums[curr] == 2) {
                // interchange nums[curr] with nums[end]
                int temp = nums[curr];
                nums[curr] = nums[end];
                nums[end] = temp;
                end--;
            }else if (nums[curr] == 1) {
                curr++;
            }else {
                // interchange nums[curr] with nums[start]
                int temp = nums[curr];
                nums[curr] = nums[start];
                nums[start] = temp;
                start++;
                curr++;
            }
        }

    }
}
