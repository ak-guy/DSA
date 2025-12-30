# Using Recursion
class Solution:
    def rightSideView(self, root):
        res = []

        def dfs(root, level):
            if not root:
                return

            if level == len(res):
                res.append(root.val)

            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 0)
        return res


# Without using recursion
from collections import deque


class Solution:
    def rightSideView(self, root):
        def sol(root):
            q = deque()
            q.append(root)
            res = []

            while q:
                len_q = len(q)
                for i in range(len_q):
                    node = q.popleft()
                    if node:
                        if i == len_q - 1:
                            res.append(node.val)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
            return res

        res = sol(root)
        return res
