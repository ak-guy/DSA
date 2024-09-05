package Misc;

import java.util.*;
/*
 * 2641. Cousins in Binary Tree II
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode replaceValueInTree(TreeNode root) {
        root.val = 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while(!q.isEmpty()){
            int nextLevelSum = 0;
            int qSize = q.size();
            List<TreeNode> parents = new ArrayList<>(q);
            for (int i=0; i<qSize; ++i) {
                TreeNode node = q.poll();
                if (node.left != null) {
                    q.offer(node.left);
                    nextLevelSum += node.left.val;
                }
                if (node.right != null) {
                    q.offer(node.right);
                    nextLevelSum += node.right.val;
                }
            }
            
            // iterating over all the values present in q as of now
            for (TreeNode n: parents) {
                int tempNextLevelSum = nextLevelSum;
                tempNextLevelSum -= n.left != null ? n.left.val : 0;
                tempNextLevelSum -= n.right != null ? n.right.val : 0;

                if (n.left != null) {n.left.val = tempNextLevelSum;}
                if (n.right != null) {n.right.val = tempNextLevelSum;}
            }
        }
        return root;
    }
}
