package Misc;

/*
 * 2285. Maximum Total Importance of Roads
 */

 import java.util.*;
 
 class Solution {
    public long maximumImportance(int n, int[][] roads) {
        int[] outGoingRoads = new int[n];

        for (int[] road: roads) {
            outGoingRoads[road[0]]++;
            outGoingRoads[road[1]]++;
        }

        Arrays.sort(outGoingRoads);
        long res = 0;
        long start = 1;
        for (int val: outGoingRoads) {
            res += (val*start);
            start++;
        }

        return res;
    }
}

class Dummy {
    
}
