from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def traverse(root):
            nonlocal res
            if not root:
                return 0

            left_val = traverse(root.left)
            right_val = traverse(root.right)

            res += abs(left_val + right_val + root.val - 1)

            # return value will be -ve if the node requires coin but it will be +ve if it is giving coins
            return left_val + right_val + root.val - 1

        traverse(root)
        return res
