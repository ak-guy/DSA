// package Misc;
/*
 * 1609. Even Odd Tree
 */
import java.util.*;

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
    public boolean isEvenOddTree(TreeNode root) {
        if (root == null || (root != null && (root.val & 1) == 0)) return false;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int level=0;
        while (!q.isEmpty()) {
            int qSize = q.size();
            int prevVal = (level & 1) == 0 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            for (int i=0; i<qSize; i++) {
                TreeNode node = q.remove();
                if (node.left != null) {
                    if ((node.left.val & 1) != (level & 1) || ((level & 1) == 0 && node.left.val >= prevVal) || ((level & 1) == 1 && node.left.val <= prevVal)) return false;
                    prevVal = node.left.val;
                    q.offer(node.left);
                }
                if (node.right != null) {
                    if ((node.right.val & 1) != (level & 1) || ((level & 1) == 0 && node.right.val >= prevVal) || ((level & 1) == 1 && node.right.val <= prevVal)) return false;
                    prevVal = node.right.val;
                    q.offer(node.right);
                }
            }
            level++;
        }
        return true;
    }
}