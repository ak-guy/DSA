# without using recursion
from collections import deque
def LeftView(root):
    def sol(root):
        q = deque()
        q.append(root)
        res = []
        
        while q:
            len_q = len(q)
            for i in range(len_q):
                node = q.popleft()
                if node:
                    if i == 0:
                        res.append(node.data)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return res
        
    res = sol(root)
    return res



# Using recursion
def LeftView(root):
    def sol(root, level):
        if not root:
            return
        
        if level == len(res):
            res.append(root.data)
        
        sol(root.left, level+1)
        sol(root.right, level+1)
        
        
    res = []
    sol(root, 0)
    return res