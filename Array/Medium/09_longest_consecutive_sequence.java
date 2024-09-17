package Array.Medium;

import java.util.*;
import java.util.stream.Collectors;

/*
 * 128. Longest Consecutive Sequence
 */

class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> s = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        int res = 0;
        for (int num : nums) {
            // picking first element
            if (!s.contains(num-1)) {
                int possibleRes = 0;
                while (s.contains(num)) {
                    possibleRes++;
                    num++;
                }
                res = Math.max(res, possibleRes);
            }
        }
        return res;
    }
}