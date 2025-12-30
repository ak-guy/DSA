class Solution:
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [0, True]

            var1 = dfs(root.left)
            var2 = dfs(root.right)
            new = (var1[1] and var2[1]) and (abs(var1[0] - var2[0]) < 2)
            return [1 + max(var1[0], var2[0]), new]

        return dfs(root)[1]


# see driver code from gfg
