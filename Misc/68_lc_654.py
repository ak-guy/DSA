"""
654. Maximum Binary Tree
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """constructs binary tree"""
        tree_root = None

        def helper(start_index, end_index, n):
            nonlocal tree_root
            if start_index < 0 or end_index >= n or end_index - start_index < 0:
                return
            max_val = max(nums[start_index : end_index + 1])
            max_val_index = nums.index(max_val)

            root = TreeNode(max_val)
            if end_index - start_index == n - 1:
                tree_root = root
            root.left = helper(start_index, max_val_index - 1, n)
            root.right = helper(max_val_index + 1, end_index, n)

            return root

        n = len(nums)
        helper(0, n - 1, n)

        return tree_root
