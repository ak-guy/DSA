# # Method - 1 (Brute Force)
class Solution:
    '''
    a celebrity will have entire row elements to be 0 and all M[r][constant_column] = 1
    '''
    def celebrity(self, M, n):
        res = -1
        
        # to get list of all rows where every element is zero
        possible_celeb = []
        for r in range(n):
            flag = True
            for c in range(n):
                if M[r][c] != 0:
                    flag = False
                    break
            if flag:
                possible_celeb.append(r)
        
        # for every possible_celeb we will check for every rol
        for c in possible_celeb:
            flag = True
            for row in range(n):
                if M[row][c] != 1 and row != c:
                    flag = False
                    break
            if flag:
                res = c
                return res
            
        return -1
    
# # Method - 2 (Using Stack)
class Solution:
    '''
    a celebrity will have entire row elements to be 0 and all M[r][constant_column] = 1
    '''
    def celebrity(self, M, n):
        st = []
        for i in range(n):
            st.append(i)
            
        # get possible celeb
        while len(st) > 1:
            first = st.pop()
            second = st.pop()
            
            # case 1: first knows second
            if M[first][second] == 1:
                st.append(second)
            else:
                st.append(first)
        
        # now we got one possible celebrity (see at last, stack will have only one element)
        
        # checking if all row is zero
        rowcheck = True
        for i in range(n):
            if M[st[-1]][i] != 0:
                rowcheck = False
                break

        # checking if all col is one 
        colcheck = True
        for i in range(n):
            if i != st[-1] and M[i][st[-1]] != 1:
                colcheck = False
                break
                
        if rowcheck and colcheck:
            return st[-1]
        return -1