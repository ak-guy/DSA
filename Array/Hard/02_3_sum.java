package Array.Hard;
import java.util.*;

/*
 * 15. 3Sum
 */

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i=0; i<n; i++) {
            int curr = nums[i];
            if (i>0 && nums[i-1]==curr) continue;
            // applying two pointer
            int start=i+1;
            int end=n-1;
            while (start<end) {
                int summ = curr + nums[start] + nums[end];
                if (summ == 0) {
                    List<Integer> temp = new ArrayList<>();
                    temp.add(curr);
                    temp.add(nums[start]);
                    temp.add(nums[end]);
                    res.add(temp);
                    start++;
                    while (nums[start]==nums[start-1] && start<end) start++;
                }else if (summ < 0) {
                    start++;
                }else {
                    end--;
                }
            }
        }
        return res;
    }
}