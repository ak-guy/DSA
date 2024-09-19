package Array.Hard;
import java.util.*;

/*
 * 18. 4Sum
 */

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int n = nums.length;
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i=0; i<n-3; i++) {
            int first = nums[i];
            if (i>0 && nums[i-1]==first) continue;
            for (int j=i+1; j<n-2; j++) {
                int curr = nums[j];
                if (j>i+1 && nums[j-1]==curr) continue;
                // applying two pointer
                int start=j+1;
                int end=n-1;
                while (start<end) {
                    long summ = (long) first + (long) curr + (long) nums[start] + (long) nums[end];
                    if (summ == (long) target) {
                        List<Integer> temp = new ArrayList<>();
                        temp.add(first);
                        temp.add(curr);
                        temp.add(nums[start]);
                        temp.add(nums[end]);
                        res.add(temp);
                        start++;
                        while (start<end && nums[start]==nums[start-1]) start++;
                    }else if (summ < target) {
                        start++;
                    }else {
                        end--;
                    }
                }
            }
            
        }
        return res;
    }
}