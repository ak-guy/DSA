from collections import defaultdict


class Solution:
    def minTime(self, root, target):
        # same as finding all nodes at distance k from target node
        if not root.left and not root.right:
            return 0

        gr = defaultdict(list)

        def makeGraph(root, prev):
            if not root:
                return

            if prev:
                gr[root.data].append(prev)
            if root.left:
                gr[root.data].append(root.left.data)
            if root.right:
                gr[root.data].append(root.right.data)

            makeGraph(root.left, root.data)
            makeGraph(root.right, root.data)

        makeGraph(root, None)

        count = 0
        res = [target]
        visited = set(res)
        while len(visited) != len(gr):
            new_result = []
            for parent_node in res:
                for child_node in gr[parent_node]:
                    if child_node not in visited:
                        new_result.append(child_node)
            res = new_result
            visited |= set(res)
            count += 1

        return count
