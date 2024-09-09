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


// Optimized approach
class CBTInserter2 {
    List<TreeNode> listRep;
    public CBTInserter2(TreeNode root) {
        this.listRep = new ArrayList<>();
        this.listRep.add(root);
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int qSize = q.size();
            for (int i=0; i<qSize; i++) {
                TreeNode node = q.remove();
                if (node.left != null) {
                    q.offer(node.left);
                    this.listRep.add(node.left);
                }
                if (node.right != null) {
                    q.offer(node.right);
                    this.listRep.add(node.right);
                }
            }
        }
    }
    
    public int insert(int val) {
        TreeNode node = new TreeNode(val);
        listRep.add(node);
        int listRepSize = listRep.size();
        TreeNode parent = listRep.get(listRepSize/2 - 1);
        if (parent.left == null) parent.left = node;
        else if (parent.right == null) parent.right = node;

        return parent.val; 
    }
    
    public TreeNode get_root() {
        return this.listRep.get(0);
    }
}