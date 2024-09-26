'''
655. Print Binary Tree
All math was given in problem statement itself
'''


import math
from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getHeight(self, root):
        if not root:
            return 0

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        h = self.getHeight(root)
        res = [["" for _ in range(int(math.pow(2, h))-1)] for _ in range(h)]

        res[0][len(res[0]) // 2] = str(root.val)

        q = deque()
        q.append((root,0,len(res[0]) // 2))
        while q:
            qSize = len(q)
            for i in range(qSize):
                node, r, c = q.popleft()
                if r==h: break
                if (node.left):
                    newR = r+1
                    newC = c-int(math.pow(2, h-r-2))
                    res[newR][newC] = str(node.left.val)
                    q.append((node.left, newR, newC))
                if (node.right):
                    newR = r+1
                    newC = c+int(math.pow(2, h-r-2))
                    res[newR][newC] = str(node.right.val)
                    q.append((node.right, newR, newC))
        
        return res