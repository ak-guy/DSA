# Function to return the ceil of given number in BST.


class Solution:
    def findCeil(self, root, inp):
        # code here
        res = -1
        while root:
            if root.key >= inp:
                res = root.key
                root = root.left
            else:
                root = root.right

        return res
