package Array.Easy;

import java.util.*;
/*
 * 560. Subarray Sum Equals K
 */
class Solution {
    public int subarraySum(int[] nums, int k) {
        /*
        run the algorithm through this example to get deeper understanding
        eg - nums = [5,1,-10,2,8,6,-8,20,-11] and k = 6

        Also the reason why we are searching runningSum - k in hmap is because
        we want to know if including current val can we find the number x which when
        substracted from runningSum equals k
        runningSum - x = k
        x = runningSum - k
        in other words x => sum(nums[:some_index])
        */      
        int runningSum = 0;
        Map<Integer, Integer> sumVsCount = new HashMap<>();
        sumVsCount.put(0,1);
        int res = 0;
        for (int i=0; i<nums.length; i++) {
            runningSum += nums[i];
            int diff = runningSum - k;
            res += sumVsCount.getOrDefault(diff, 0);
            sumVsCount.put(runningSum, sumVsCount.getOrDefault(runningSum, 0)+1);
        }

        return res;
    }
}