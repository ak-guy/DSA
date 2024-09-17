package Array.Medium;

/*
 * 31. Next Permutation
 */

class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int endIndex = n-1;
        while (endIndex >= 0) {
            if (endIndex != 0 && nums[endIndex] > nums[endIndex-1]) {
                endIndex--;
                break;
            }
            endIndex--;
        }

        // edge case where the given permutation is last permutation possible
        if (endIndex == -1) {
            endIndex++;
            int end = n-1;
            while (endIndex < end) {
                int t = nums[endIndex];
                nums[endIndex] = nums[end];
                nums[end] = t;
                endIndex++;
                end--;
            }
            return;
        }
        
        // getting the index of element with which we have to interchange nums[endIndex]
        int toExchangeIndex = n-1;
        while (nums[endIndex] >= nums[toExchangeIndex]) {
            toExchangeIndex--;
        }

        int temp = nums[endIndex];
        nums[endIndex] = nums[toExchangeIndex];
        nums[toExchangeIndex] = temp; 

        // reverse the array after endIndex
        endIndex++;
        int newEndIndex = n-1;
        while (endIndex < newEndIndex) {
            // System.out.print(endIndex+" "+ newEndIndex);
            int newTemp = nums[endIndex];
            nums[endIndex] = nums[newEndIndex];
            nums[newEndIndex] = newTemp;
            endIndex++;
            newEndIndex--;
        }

    }
}