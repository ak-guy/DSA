package Array.Hard;
import java.util.*;

/*
 * 56. Merge Intervals
 */
class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length==1) return intervals;
        Arrays.sort(intervals, Comparator.comparingInt(x -> x[0]));
        
        int n = intervals.length;
        int[][] res = new int[n][2];

        int currPointer = 0; // this counter will tell many intervals are there 
        res[currPointer][0] = intervals[0][0];
        res[currPointer][1] = intervals[0][1];

        for (int i=1; i<intervals.length; i++) {
            int lastEnd = res[currPointer][1];
            if (intervals[i][0] <= lastEnd) {
                res[currPointer][1] = Math.max(lastEnd, intervals[i][1]);
            }else {
                currPointer++;
                res[currPointer][0] = intervals[i][0];
                res[currPointer][1] = intervals[i][1];
            }
        }

        // just picking values that matter
        int[][] ans = new int[currPointer+1][2];
        for (int i=0; i<=currPointer; i++) {
            ans[i][0] = res[i][0];
            ans[i][1] = res[i][1];
        }
        
        return ans;
    }
}