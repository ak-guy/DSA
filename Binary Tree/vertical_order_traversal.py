# Could not handle this case :
# # There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.


from collections import defaultdict,deque
class Solution:
    def verticalTraversal(self, root):
        # dic = {} -> vertical_level(integer) : root_val(list)
        minn_level = 1e10
        maxx_level = -1e10

        def levelorder(root):
            nonlocal minn_level
            nonlocal maxx_level
            res = []
            q = deque()
            q.append((root, 0))
            dic = defaultdict(list)

            while q:
                dummy_dict = defaultdict(list)
                for i in range(len(q)):
                    node, vals = q.popleft()
                    if node:
                        minn_level = min(minn_level, vals)
                        maxx_level = max(maxx_level, vals)
                        dummy_dict[str(vals)].append(node.val)
                        q.append((node.left, vals-1))
                        q.append((node.right, vals+1))
            return dic

        ans = levelorder(root)
        res = []
        for i in range(minn_level, maxx_level+1):
            res.append(ans[str(i)])
            
        return res