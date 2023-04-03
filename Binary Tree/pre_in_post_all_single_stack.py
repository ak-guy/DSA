# # Algo : 
# 1. In stack we will store [node, some_int] some_int will tell us where we need to put node.val

# 2. for '1' -> we will put the val in preorder and increment the some_value by one and push it once more in stack also if there exists a left then we will also add it in stack with some_int = 1

# 3. for '2' -> we will put the val in inorder and increment the some_value by one and push it once more in stack also if there exists a right then we will also add it in stack with some_int = 1

# 4. for '3' -> for this we only need to put the val in postorder

def pre_in_post(root):
    st = []
    st.append([root, 1])
    preorder, inorder, postorder = [], [], []

    while st:
        var = st.pop()

        if var[1]==1: # preorder
            preorder.append(var[0].val)
            st.append([var[0], 2])
            if var[0].left:
                st.append([var[0].left, 1])

        elif var[1]==2: # inorder
            inorder.append(var[0].val)
            st.append([var[0], 3])
            if var[0].right:
                st.append([var[0].right, 1])

        elif var[1]==3: # postorder
            postorder.append(var[0].val)
    
    return preorder, inorder, postorder