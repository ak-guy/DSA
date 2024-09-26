/*
 * 1615. Maximal Network Rank
 */

 import java.util.*;

 class Solution {
     public int maximalNetworkRank(int n, int[][] roads) {
         Set<String> existingRoads = new HashSet<>();
         int[] nodeVsNeighbourCount = new int[n];
 
         for (int[] road : roads) {
             existingRoads.add(road[0] + "," + road[1]);
             existingRoads.add(road[1] + "," + road[0]); // Add both directions
             nodeVsNeighbourCount[road[0]]++;
             nodeVsNeighbourCount[road[1]]++;
         }
 
         int res = 0;
         for (int city1 = 0; city1 < n - 1; city1++) {
             for (int city2 = city1 + 1; city2 < n; city2++) {
                 int count = nodeVsNeighbourCount[city1] + nodeVsNeighbourCount[city2];
                 if (existingRoads.contains(city1 + "," + city2)) {
                     count--; // Subtract 1 if there is a direct road
                 }
                 res = Math.max(res, count);
             }
         }
 
         return res;
     }
 }
 