package Misc;

/*
 * 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
 */

import java.util.*;

class Solution {
    private int getMinimumCitiesReachable(int city, Map<Integer, List<int[]>> gr, int distanceThreshold, int n) {
        int[] resArray = new int[n];
        Arrays.fill(resArray, Integer.MAX_VALUE);
        boolean[] reachableCity = new boolean[n];
        int res = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[] {0,city});
        resArray[city] = 0;

        while (!pq.isEmpty()) {
            int[] first = pq.poll();
            int totalDistance = first[0];
            int node = first[1];

            for (int[] it: gr.get(node)) {
                int neighbour = it[0];
                int weight = it[1];

                if (totalDistance + weight < resArray[neighbour]) {
                    resArray[neighbour] = totalDistance + weight;
                    if (!reachableCity[neighbour] && resArray[neighbour] <= distanceThreshold) {
                        res++;
                        reachableCity[neighbour] = true;
                    }
                    pq.offer(new int[] {resArray[neighbour], neighbour});
                }
            }
        }
        return res;
    }

    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        Map<Integer, List<int[]>> gr = new HashMap<>();
        for (int[] edge : edges) {
            gr.computeIfAbsent(edge[0], v -> new ArrayList<>()).add(new int[] {edge[1], edge[2]});
            gr.computeIfAbsent(edge[1], v -> new ArrayList<>()).add(new int[] {edge[0], edge[2]});
        }
        
        int minCitiesReachable = Integer.MAX_VALUE;
        int res = 0;
        for (int city=0; city<n; city++) {
            int citiesReachable = gr.containsKey(city) ? getMinimumCitiesReachable(city, gr, distanceThreshold, n) : 0;
            if (citiesReachable < minCitiesReachable) {
                minCitiesReachable = citiesReachable;
                res = city;
            } else if (citiesReachable == minCitiesReachable) {
                res = city;
            }
        }

        return res;
    }
}