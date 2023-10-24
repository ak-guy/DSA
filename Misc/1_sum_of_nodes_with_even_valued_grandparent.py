# # Method - 1 (Brute Force)
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root):
        # arr = [root]
        value = 0
        count = 2
        q = deque()
        q.append(root)
        while q and count:
            n = len(q)
            for i in range(n):
                _root = q.popleft()
                if _root.left:
                    q.append(_root.left)
                if _root.right:
                    q.append(_root.right)
            count -= 1

        while q:
            value += q.pop().val
        return value

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def traverse(root):
            nonlocal res
            if not root:
                return
            traverse(root.left)
            traverse(root.right)

            if root and root.val % 2 == 0:
                res += self.helper(root)
            
        traverse(root)
        return res
    

# # Method - 2 (without using helper function)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def traverse(root: TreeNode, parent: TreeNode, grandparent: TreeNode):
            nonlocal res
            if not root:
                return
            
            traverse(root.left, root, parent)
            traverse(root.right, root, parent)

            if root and parent and grandparent and grandparent.val % 2 == 0:
                res += root.val
        
        traverse(root, None, None)
        return res