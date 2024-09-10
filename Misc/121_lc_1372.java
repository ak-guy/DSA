package Misc;

/*
 * 1372. Longest ZigZag Path in a Binary Tree
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
    public int longestZigZag(TreeNode root) {
        return dfs(root)[2];
    }

    private int[] dfs(TreeNode root) {
        // left = max zig zag possible from left subTree
        // right = max zig zag possible from right subTree
        // res = max zig zag possible for entire tree
        
        if (root == null) return new int[] {-1, -1, -1};
        int[] leftSubTreeResult = dfs(root.left);
        int[] rightSubTreeResult = dfs(root.right);

        int left = leftSubTreeResult[1]+1;
        int right = rightSubTreeResult[0]+1;
        int res = Math.max(Math.max(left, right), Math.max(leftSubTreeResult[2], rightSubTreeResult[2]));
        return new int[] {left, right, res};
    }
}