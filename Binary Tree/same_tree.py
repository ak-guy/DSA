class Solution:
    # Function to check if two trees are identical.
    def isIdentical(self, root1, root2):
        # Code here
        def sol(root1, root2):
            # base conditions
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False

            left = sol(root1.left, root2.left)
            right = sol(root1.right, root2.right)

            return root1.data == root2.data and left and right

        return sol(root1, root2)
