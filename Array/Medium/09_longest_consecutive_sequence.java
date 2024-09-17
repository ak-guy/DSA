package Array.Medium;

import java.util.*;
import java.util.stream.Collectors;

/*
 * 128. Longest Consecutive Sequence
 * Important thing to remember is that we only need to check for further elements
 * if the current element is the starting number of subsequence that we can confirm
 * by checking in set whether num-1 exists or not
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