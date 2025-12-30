class Solution:
    # Function to check whether all nodes of a tree have the value
    # equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        def sol(root):
            if not root:
                return [True, 0]

            left = sol(root.left)
            right = sol(root.right)

            if root.left and root.right:
                return [
                    root.data == (left[1] + right[1]) and left[0] and right[0],
                    root.data,
                ]
            elif root.left:
                return [root.data == left[1] and left[0] and right[0], root.data]
            elif root.right:
                return [root.data == right[1] and left[0] and right[0], root.data]
            else:
                return [True, root.data]

        boolean, val = sol(root)

        return 1 if boolean == True else 0
