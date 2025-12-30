"""
1008. Construct Binary Search Tree from Preorder Traversal
"""

from typing import List, Optional, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findJustGreaterThanRootValue(
        self, val: int, start_index: int, end_index: int, preorder: List[int]
    ) -> int:
        for ind in range(start_index + 1, end_index + 1):
            if preorder[ind] > val:
                return ind
        return None

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        def helper(start_index, end_index) -> Any[TreeNode, None]:
            if end_index - start_index < 0:
                return
            if end_index == start_index:
                return TreeNode(preorder[start_index])

            root = TreeNode(preorder[start_index])
            right_subtree_starting_index = self.findJustGreaterThanRootValue(
                preorder[start_index], start_index, end_index, preorder
            )

            if (
                right_subtree_starting_index
                and right_subtree_starting_index - start_index > 1
            ):
                root.left = helper(start_index + 1, right_subtree_starting_index - 1)
            elif not right_subtree_starting_index:
                root.left = helper(start_index + 1, end_index)

            if right_subtree_starting_index:
                root.right = helper(right_subtree_starting_index, end_index)

            return root

        return helper(0, n - 1)
