'''
2265. Count Nodes Equal to Average of Subtree
'''

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAverage(self, sum: int, k: int) -> int:
        return sum//k

    def averageOfSubtree(self, root: TreeNode) -> List[int]:
        res = 0
        def helper(root) -> int:
            ''' params: 
                root: TreeNode

                output:
                [total_subtree_sum, number_of_nodes]
            '''
            nonlocal res
            if not root: return [0, 0]

            if not root.left and not root.right:
                res += 1
                return [root.val, 1]
            
            left_subtree_sum, left_subtree_nodes = helper(root.left)
            right_subtree_sum, right_subtree_nodes = helper(root.right)
            
            total_value = root.val + left_subtree_sum + right_subtree_sum
            total_nodes = left_subtree_nodes + right_subtree_nodes + 1
            # print(f'currently traversing root val = {root.val} and total_value = {total_value}, total_nodes = {total_nodes}') # for debug 
            if self.getAverage(total_value, total_nodes) == root.val:
                res += 1

            return [total_value, total_nodes]
        
        helper(root)
        return res