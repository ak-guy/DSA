from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def traverse(root):
            if not root:
                return

            traverse(root.left)
            traverse(root.right)
            if (
                root.left
                and root.left.val == target
                and root.left.left is None
                and root.left.right is None
            ):
                root.left = None
            if (
                root.right
                and root.right.val == target
                and root.right.left is None
                and root.right.right is None
            ):
                root.right = None

        traverse(root)

        # handling the case where we have to remove whole tree
        if root.val == target and not root.left and not root.right:
            return None

        return root
