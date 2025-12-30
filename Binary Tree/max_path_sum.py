class Solution:
    # Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root):
        # Your code here
        res = -1e10

        def sol(root):
            nonlocal res

            if not root:
                return 0

            left = sol(root.left)
            right = sol(root.right)

            left = max(left, 0)
            right = max(right, 0)

            max_sum_including_this_node = root.data + max(left, right)

            res = max(res, root.data + left + right)

            return max_sum_including_this_node

        sol(root)

        return res
