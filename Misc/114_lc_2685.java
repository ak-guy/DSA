package Misc;

/*
 * 2685. Count the Number of Complete Components
 */
import java.util.*;
class Solution {
    private void dfs(int node, Map<Integer, List<Integer>> gr, int[] visited, int[] numberNodes, int[] numberEdges) {
        visited[node] = 1;
        numberNodes[0]++;
        numberEdges[0] += gr.get(node).size();
        for (int neighbour: gr.getOrDefault(node, new ArrayList<>())) {
            if (visited[neighbour] == 0) {
                dfs(neighbour, gr, visited, numberNodes, numberEdges);
            }
        }
    }

    public int countCompleteComponents(int n, int[][] edges) {
        int[] visited = new int[n];
        int res = 0;
        Map<Integer, List<Integer>> gr = new HashMap<>();
        for (int[] edge : edges) {
            gr.putIfAbsent(edge[0], new ArrayList<>());
            gr.putIfAbsent(edge[1], new ArrayList<>());

            gr.get(edge[0]).add(edge[1]);
            gr.get(edge[1]).add(edge[0]);
        }

        for (int i=0; i<n; i++) {
            if (visited[i] == 0 && gr.containsKey(i)) {
                int[] numberNodes = new int[1];
                int[] numberEdges = new int[1];
                dfs(i, gr, visited, numberNodes, numberEdges); // passing numberNodes and numberEdges by reference so that we can actually change its value during dfs execution
                if (numberNodes[0] * (numberNodes[0]-1) == numberEdges[0]) {
                    res++;
                }
            }
            else if (!gr.containsKey(i)) res++;
        }
        return res;
    }
}