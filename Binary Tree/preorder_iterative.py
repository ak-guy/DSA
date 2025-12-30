def preorderTraversal(self, root):
    st = []
    res = []

    st.append(root)
    while st:
        var = st.pop()
        if var:
            res.append(var.val)
            st.append(var.right)
            st.append(var.left)

    return res
