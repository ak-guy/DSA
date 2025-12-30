class Solution:
    def checkHeight(self, root):
        def leftHeight(root):
            if not root:
                return 0

            return 1 + leftHeight(root.left)

        def rightHeight(root):
            if not root:
                return 0

            return 1 + rightHeight(root.right)

        return [leftHeight(root) == rightHeight(root), leftHeight(root)]

    def countNodes(self, root) -> int:
        def sol(root):
            if not root:
                return 0

            val = self.checkHeight(root)
            if val[0]:
                return 2 ** val[1] - 1

            left = sol(root.left)
            right = sol(root.right)

            return 1 + left + right

        return sol(root)
