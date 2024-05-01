# Definition for a binary tree node.
from __future__ import annotations

from collections import defaultdict
from collections import deque
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        q = deque()
        q.append((root, 0, 0))  # root_node, col, height
        # {main_key : {sub_key: [values]}}
        mappings = defaultdict(lambda: defaultdict(list))
        leftmost_col = 10000001
        rightmost_col = -10000001
        while q:
            for i in range(len(q)):
                node, col, height = q.popleft()
                if node:
                    leftmost_col = min(leftmost_col, col)
                    rightmost_col = max(rightmost_col, col)
                    mappings[col][height].append(node.val)
                    q.append((node.left, col-1, height+1))
                    q.append((node.right, col+1, height+1))

        total_cols = rightmost_col - leftmost_col + 1
        res = [[] for i in range(total_cols)]

        for key, val in mappings.items():
            for new_key, new_val in val.items():
                some_index = abs(leftmost_col) + key
                res[some_index].extend(sorted(new_val))

        return res
