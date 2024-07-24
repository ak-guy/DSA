'''
1382. Balance a Binary Search Tree
'''

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBalancedBSTFromSortedArray(self, arr: List[int]) -> TreeNode:
        def helper(start_index, end_index):
            if end_index < start_index:
                return
            if end_index == start_index:
                return TreeNode(arr[end_index])

            mid = (end_index + start_index) // 2
            root = TreeNode(arr[mid])
            root.left = helper(start_index, mid-1)
            root.right = helper(mid+1, end_index)

            return root

        return helper(0, len(arr)-1)

    def balanceBST(self, root: TreeNode) -> TreeNode:
        bst_values = []
        def dfs(root):
            if root.left:
                dfs(root.left)
            bst_values.append(root.val)
            if root.right:
                dfs(root.right)

        dfs(root)

        return self.createBalancedBST(bst_values)