package Array.Medium;
import java.util.*;
/*
 * 1. Two Sum
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> valueVsIndex = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            int diff = target - nums[i];
            if (valueVsIndex.containsKey(diff)) {
                return new int[] {valueVsIndex.get(diff), i};
            }
            valueVsIndex.put(nums[i], i);
        }
        return new int[] {};
    }
}