def inorderTraversal(self, root):
    st = []
    res = []
    curr = root
    # st.append(root)
    while st or curr:
        while curr:
            st.append(curr)
            curr = curr.left

        curr = st.pop()
        res.append(curr.val)
        curr = curr.right

    return res
