# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        postorder = postorder[::-1]

        def sol(post, ino):
            if not post and not ino:
                return None

            mid_val = ino.index(post[0])
            root = TreeNode(post[0])

            root.left = sol(post[len(post) - mid_val :], ino[:mid_val])
            root.right = sol(post[1 : len(post) - mid_val], ino[mid_val + 1 :])

            return root

        return sol(postorder, inorder)
