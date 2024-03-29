class Solution:
    '''
    similar as pref to inf conversion, make a stack, traverse in **forward**, will store res in stack so final ans will be st.pop()
    if we encounter alnum then directly append it to stack
    else if operator is encountered then st.append(str(  '(' +second+operator+first+ ')'  ))
    '''
    def postToInfix(self, postfix):
        st = []
        for char in postfix:
            if char.isalnum():
                st.append(char)
            else:
                first = st.pop()
                second = st.pop()
                res = str('(' + second + char + first + ')')
                st.append(res)
        
        return st.pop()