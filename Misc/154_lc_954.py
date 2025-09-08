'''
958. Check Completeness of a Binary Tree
'''

'''
This solution determines if a binary tree is complete by first calculating its 
height recursively, then performing a level-order traversal using a queue. At 
each level, it ensures that all missing nodes (null children) are explicitly 
represented by placeholder nodes with a special value (-1). During traversal, 
if a node with a negative value (-1) is encountered followed by a valid node, 
it returns false, indicating the tree is not complete. By forcing each level 
to have the full breadth with placeholders and then checking the order of these 
placeholder nodes against real nodes, the algorithm verifies the completeness 
condition that every level except possibly the last is fully filled and all nodes 
are as far left as possible. If no violations are found, it returns true.
'''

# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getHeight(self, root) -> int:
        if not root:
            return 0
        return max(1 + self.getHeight(root.left), 1 + self.getHeight(root.right))

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        tree_height = self.getHeight(root)
        
        q = deque()
        q.append(root)
        
        prev_node_val = 1
        curr_height = 0
        while q:
            total_nodes_at_level = len(q)
            curr_height += 1
            for _ in range(total_nodes_at_level):
                curr_root = q.popleft()
                if prev_node_val < 0 and curr_root.val > 0:
                    return False

                if curr_root.left:
                    q.append(curr_root.left)
                elif curr_height < tree_height:
                    new_node = TreeNode(-1)
                    q.append(new_node)

                if curr_root.right:
                    q.append(curr_root.right)
                elif curr_height < tree_height:
                    new_node = TreeNode(-1)
                    q.append(new_node)
                
                prev_node_val = curr_root.val
        
        return True