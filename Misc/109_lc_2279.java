package Misc;

/*
 * 2279. Maximum Bags With Full Capacity of Rocks
 */
import java.util.*;

class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int n = rocks.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int res = 0;
        for (int i=0; i<n; i++) {
            int spaceAvailable = capacity[i]-rocks[i];
            if (spaceAvailable > 0) {
                pq.offer(spaceAvailable);
            }else {
                res++;
            }
        }

        while (res<n && additionalRocks>0) {
            int minDiff = pq.poll();
            additionalRocks -= minDiff;
            if (additionalRocks >= 0) {res++;}
            else {break;}
        }

        return res;
    }
}