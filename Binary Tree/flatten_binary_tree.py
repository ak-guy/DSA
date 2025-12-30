# # Method 1 => Using Recuesion


class Solution:
    def flatten(self, root):
        prev_node = None

        def sol(root):
            nonlocal prev_node
            if not root:
                return

            sol(root.right)
            sol(root.left)

            root.right = prev_node
            root.left = None
            prev_node = root

        sol(root)
