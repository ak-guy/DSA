from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root: TreeNode):
        '''
        return length of a subtree and (TreeNode) lca of deepest leaves for that subtree 

        Algo: we will traverse the tree in postorder, then validate both children of a parent node
              if we receive same height from both nodes then our root will be lca
        '''
        if not root:
            return 0, None
        left, right = self.helper(root.left), self.helper(root.right)
        if left[0] > right[0]:
            # height of left child is greater
            return left[0] + 1, left[1]
        elif right[0] > left[0]:
            # height of right child is greater
            return right[0] + 1, right[1]
        else:
            # received same height from children nodes
            return left[0]+1, root

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_tree_height, lca_of_deepest_leaves = self.helper(root)
        return lca_of_deepest_leaves