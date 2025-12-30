"""
814. Binary Tree Pruning
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postorder(root):
            if not root:
                return False
            if not root.left and not root.right and root.val == 0:
                return False

            left = postorder(root.left)
            right = postorder(root.right)

            if not left:
                root.left = None
            if not right:
                root.right = None

            return left or right or root.val

        postorder(root)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root
