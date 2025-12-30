from collections import deque


class Solution:
    def widthOfBinaryTree(self, root):
        # using indexing logic from segment tree
        # for 1 based indexing -> left_val = root_val*2 and right_val = root_val*2 + 1
        # for 0 based indexing -> left_val = root_val*2 + 1 and right_val = root_val*2 + 2

        if not root:
            return 0

        q = deque()
        q.append((root, 1))  # root, num

        ans = 0
        while q:
            initial = None
            final = None
            size = len(q)
            for i in range(size):
                node, num = q.popleft()
                if i == 0:
                    initial = num
                if i == size - 1:
                    final = num

                if node.left:
                    q.append((node.left, num * 2))
                if node.right:
                    q.append((node.right, num * 2 + 1))

            ans = max(ans, final - initial + 1)

        return ans
