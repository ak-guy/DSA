package Misc;

/*
 * 919. Complete Binary Tree Inserter
 */

// brute force
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

class CBTInserter {
    private TreeNode root;
    public CBTInserter(TreeNode root) {
        this.root = root;
    }
    
    public int insert(int val) {
        if (root == null) {
            root = new TreeNode(val);
            return val;
        }

        TreeNode tempRoot = root;
        Queue<TreeNode> q = new LinkedList<>(); 
        q.offer(tempRoot);
        while (!q.isEmpty()) {
            int qSize = q.size();
            for (int i=0; i<qSize; i++)  {
                TreeNode node = q.remove();
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);

                if (node.left == null) {
                    node.left = new TreeNode(val);
                    return node.val;
                }
                if (node.right == null) {
                    node.right = new TreeNode(val);
                    return node.val;
                }
            }
        }
        return 0;
    }
    
    public TreeNode get_root() {
        return root;
    }
}


