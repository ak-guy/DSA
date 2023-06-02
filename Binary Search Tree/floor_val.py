def findCeil(self,root, inp):
    res = -1
    while root:
        if root.key > inp:
            root = root.left
        else:
            res = root.key
            root = root.right
        
    return res