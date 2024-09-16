package Array.Medium;

/*
 * 169. Majority Element
 */

class Solution {
    public int majorityElement(int[] nums) {
        /*
        Intuition behind this problem is that when we need to observe that 
        there is an element present which occurs n/2 times or more. So what 
        we can do is assume first element to be the majority element and increase
        majority count by 1, and decrease that count till it reaches zero whenever
        we encounter an element that is not majority and when it reaches zero then we can 
        say that element could be possible majority element.

        PS : This algo works only because it is for sure that there is an element which
        occurs n/2 or more times.
        */
        int majorityElement = nums[0];
        int majorityElementCount = 0;

        for (int i=0; i<nums.length; i++) {
            if (nums[i] == majorityElement) majorityElementCount++;
            else if (majorityElementCount == 0) majorityElement = nums[i];
            else majorityElementCount--;
        }
        return majorityElement;
    }
}