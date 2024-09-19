package Array.Hard;

import java.util.*;

/*
 * 229. Majority Element II
 */

class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<>();
        int firstMajority=Integer.MAX_VALUE;
        int secondMajority=Integer.MAX_VALUE;
        int firstCount=0;
        int secondCount=0;

        for (int num:nums) {
            if (firstMajority==num) {
                firstCount++;
            }else if (secondMajority==num) {
                secondCount++;
            }else if (firstCount==0) {
                firstMajority = num;
                firstCount++;
            }else if (secondCount==0) {
                secondMajority = num;
                secondCount++;
            }else {
                firstCount--;
                secondCount--;
            }
        }
        // System.out.print("firstMajority="+firstMajority+" secondMajority="+secondMajority);
        int firstMajorityCount=0;
        int secondMajorityCount=0;
        for (int num : nums) {
            if (num == firstMajority) firstMajorityCount++;
            else if (num == secondMajority) secondMajorityCount++;
        }

        if (firstMajorityCount > nums.length/3)res.add(firstMajority);
        if (secondMajorityCount > nums.length/3)res.add(secondMajority);

        return res;
    }
}