"""
1530. Number of Good Leaf Nodes Pairs
"""

from typing import Dict, List, Set
from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLeafNodes(self, root: TreeNode) -> set:
        res = set()

        def helper(root):
            if not root.left and not root.right:
                res.add(root)
                return

            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)

        helper(root)
        return res

    def convertTreeToGraph(self, root: TreeNode):
        gp = defaultdict(list)

        def helper(root):
            if not root or (not root.left and not root.right):
                return

            if root.left:
                gp[root].append(root.left)
                gp[root.left].append(root)
            if root.right:
                gp[root].append(root.right)
                gp[root.right].append(root)

            helper(root.left)
            helper(root.right)

        helper(root)
        return gp

    def bfs(
        self,
        gr: Dict[TreeNode, List],
        leaf_node: TreeNode,
        distance: int,
        leaf_nodes: Set[TreeNode],
    ) -> int:
        res = 0
        q = deque()
        q.append(leaf_node)
        visited = set()
        visited.add(leaf_node)
        while distance > 0 and q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                for tree_node in gr[node]:
                    if tree_node not in visited:
                        visited.add(tree_node)
                        q.append(tree_node)
                        if tree_node in leaf_nodes:
                            print(tree_node)
                            res += 1
            distance -= 1

        return res

    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaf_nodes = self.getLeafNodes(root)
        gr = self.convertTreeToGraph(root)

        res = 0
        for leaf_node in leaf_nodes:
            res += self.bfs(gr, leaf_node, distance, leaf_nodes)

        return int(res / 2)
