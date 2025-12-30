class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    def lca(self, root, n1, n2):
        def sol(root):
            # base case
            if not root:
                return None

            if root.data == n1 or root.data == n2:
                return root

            left = sol(root.left)
            right = sol(root.right)

            if left and right:
                return root
            elif not left and right:
                return right
            elif left and not right:
                return left
            else:
                return None

        return sol(root)
