# # Method - 1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        arbitrary_res = 0
        def traverse(root):
            nonlocal arbitrary_res
            if not root:
                return

            traverse(root.right)
            
            if root:
                root.val += arbitrary_res
                arbitrary_res = root.val

            traverse(root.left)
        
        traverse(root)
        return root