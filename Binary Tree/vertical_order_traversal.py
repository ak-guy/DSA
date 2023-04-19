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
            q.append((root, 0, 0)) # root : level or row or height : column or vertical_height 
            dic = defaultdict(lambda : defaultdict(list))

            while q:
                for i in range(len(q)):
                    node, level, col = q.popleft()
                    if node:
                        minn_level = min(minn_level, col)
                        maxx_level = max(maxx_level, col)
                        dic[str(col)][level].append(node.val)
                        dic[str(col)][level].sort()
                        q.append((node.left, level+1, col-1))
                        q.append((node.right, level+1, col+1))
            return dic

        ans = levelorder(root)
        res = []
        for i in range(minn_level, maxx_level+1):
            dummy = []
            for level in ans[str(i)]:
                dummy.extend(ans[str(i)][level])
            res.append(dummy)
            
        return res