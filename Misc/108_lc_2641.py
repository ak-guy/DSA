"""
2641. Cousins in Binary Tree II
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummyRoot = root
        dq = deque()
        dq.append((dummyRoot, None))
        hmap = {}  # level : {parent: totalChildSum}

        level = 0
        while dq:
            for _ in range(len(dq)):
                node, parent = dq.popleft()
                if node.left:
                    dq.append((node.left, node))
                if node.right:
                    dq.append((node.right, node))

                leftNodeVal = node.left.val if node.left else 0
                rightNodeVal = node.right.val if node.right else 0
                valueToUpdate = rightNodeVal + leftNodeVal
                try:
                    hmap[level + 1].update({node: valueToUpdate})
                    hmap[level + 1]["total"] = (
                        hmap.get(level + 1).get("total") + valueToUpdate
                    )
                except:
                    hmap.update({level + 1: {node: valueToUpdate}})
                    hmap[level + 1].update({"total": valueToUpdate})

                if level == 0 or level == 1:
                    node.val = 0
                else:
                    node.val = hmap[level]["total"] - hmap[level][parent]
            level += 1
        return root
