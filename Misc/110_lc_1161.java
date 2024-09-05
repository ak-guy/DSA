package Misc;

/*
 * 1161. Maximum Level Sum of a Binary Tree
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
    public int maxLevelSum(TreeNode root) {
        if (root == null) {return 0;}
        long res = root.val;
        int resLevel = 1;

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int level = 1;
        while(!q.isEmpty()) {
            int qSize = q.size();
            long dummyRes = 0;
            for(int i=0; i<qSize; i++) {
                TreeNode node = q.poll();
                if(node.left != null) {q.offer(node.left);}
                if (node.right != null) {q.offer(node.right);}
                dummyRes += node.val;
            }
            
            if (res < dummyRes) {
                res = dummyRes;
                resLevel = level;
            }
            level++;
        }
        return resLevel;
    }
}