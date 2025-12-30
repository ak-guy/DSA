from collections import deque, defaultdict


class Solution:
    def bottomView(self, root):
        minn_level = 1e10
        maxx_level = -1e10

        def levelorder(root):
            nonlocal minn_level
            nonlocal maxx_level
            res = []
            q = deque()
            q.append(
                (root, 0, 0)
            )  # root : level or row or height : column or vertical_height
            dic = defaultdict(list)

            while q:
                for i in range(len(q)):
                    node, level, col = q.popleft()
                    if node:
                        minn_level = min(minn_level, col)
                        maxx_level = max(maxx_level, col)

                        dic[str(col)] = node.data

                        q.append((node.left, level + 1, col - 1))
                        q.append((node.right, level + 1, col + 1))
            return dic

        ans = levelorder(root)
        res = []
        for i in range(minn_level, maxx_level + 1):
            res.append(ans[str(i)])

        return res
