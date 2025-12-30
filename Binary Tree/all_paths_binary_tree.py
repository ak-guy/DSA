def Paths(root):
    # don't print new line
    res = []

    def sol(root, curr):
        if not root:
            return

        curr.append(root.data)
        if not root.left and not root.right:
            res.append(curr.copy())

        sol(root.left, curr)
        sol(root.right, curr)

        curr.pop()
        return

    sol(root, [])
    # print(res)
    return res
