// package Misc;

import java.util.*;

/*
 * 1514. Path with Maximum Probability
 * Solved using Djikstra Algorithm
 */

class Solution {
    private Map<Integer, List<double[]>> makeGraph(int[][] edges, double[] succProb) {
        Map<Integer, List<double[]>> gp = new HashMap<>();
        for (int i=0; i<edges.length; i++) {
            gp.putIfAbsent(edges[i][0], new ArrayList<>());
            gp.putIfAbsent(edges[i][1], new ArrayList<>());

            double[] edge1 = new double[] {edges[i][1], succProb[i]};
            double[] edge2 = new double[] {edges[i][0], succProb[i]};

            gp.get(edges[i][0]).add(edge1);
            gp.get(edges[i][1]).add(edge2);
        } 

        return gp;
    }

    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        double[] maxProb = new double[n];
        Arrays.fill(maxProb, 0.00000);
        Map<Integer, List<double[]>> gp = makeGraph(edges, succProb);

        // max priority queue based on first value of double[]
        PriorityQueue<double[]> pq = new PriorityQueue<>(new Comparator<double[]>() {
            @Override
            public int compare(double[] a, double[] b) {
                return Double.compare(b[0], a[0]);
            }
        });

        pq.offer(new double[] {1.00000, start_node});
        while (!pq.isEmpty()) {
            double[] first = pq.poll();
            int node = (int) first[1];
            double probability = first[0];

            for (double[] neighbour: gp.getOrDefault(node, new ArrayList<>())) {
                int neighbourNode = (int) neighbour[0];
                double neighbourProb = neighbour[1];

                if (probability * neighbourProb > maxProb[neighbourNode]) {
                    maxProb[neighbourNode] = probability * neighbourProb;
                    pq.offer(new double[] {probability * neighbourProb, neighbourNode});
                }
            }
        }

        return maxProb[end_node];
    }
}