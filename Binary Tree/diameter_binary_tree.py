class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        ans = 0
        def sol(root):
            nonlocal ans
            if not root:
                return 0
            left = sol(root.left)
            right = sol(root.right)
            ans = max(ans, left + right)
            
            return 1 + max(left, right)

        sol(root)
        return ans+1
    
# see driver code from gfg