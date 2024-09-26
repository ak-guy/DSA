/*
 * 1466. Reorder Routes to Make All Paths Lead to the City Zero
 */

import java.util.*;

class Solution {
    public int minReorder(int n, int[][] connections) {
        Map<Integer, List<Integer>> directedGraph = new HashMap<>();
        Map<Integer, List<Integer>> undirectedGraph = new HashMap<>();
        
        // Build the directed and undirected graphs
        for (int[] connection : connections) {
            int fromCity = connection[0];
            int toCity = connection[1];
            directedGraph.putIfAbsent(fromCity, new ArrayList<>());
            directedGraph.get(fromCity).add(toCity);
            
            undirectedGraph.putIfAbsent(fromCity, new ArrayList<>());
            undirectedGraph.get(fromCity).add(toCity);
            undirectedGraph.putIfAbsent(toCity, new ArrayList<>());
            undirectedGraph.get(toCity).add(fromCity);
        }

        int res = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        Set<Integer> visited = new HashSet<>();
        visited.add(0);

        // BFS traversal
        while (!queue.isEmpty()) {
            int fromCity = queue.poll();
            for (int toCity : undirectedGraph.getOrDefault(fromCity, new ArrayList<>())) {
                if (!visited.contains(toCity)) {
                    if (!directedGraph.getOrDefault(toCity, new ArrayList<>()).contains(fromCity)) {
                        res++; // Need to reorder this road
                    }
                    queue.add(toCity);
                    visited.add(toCity);
                }
            }
        }

        return res;
    }
}
