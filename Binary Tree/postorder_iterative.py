def postorderTraversal(self, root):
    res = []
    st = []

    st.append(root)
    while st:
        top_node = st.pop()
        if top_node:
            res.append(top_node.val)
            st.append(top_node.left)
            st.append(top_node.right)
    
    return res[::-1]