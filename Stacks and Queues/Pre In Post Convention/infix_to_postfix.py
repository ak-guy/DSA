class Solution:
    '''
    eg ~> A*(B+C)/D  ------>   ABC+*D/
    any alphanum we can directly add to res, but we need to handle operators and brackets using mon inc stack
    
    we will create a stack in which we will only store precedence_mapping.keys() also it will be monotonically
    increasing -> -+/*^
    '''
    def InfixtoPostfix(self, exp):
        res = ""
        st = []
        precedence_mapping = {"^":4, "*":3, "/":2, "+":1, "-":1, "(":0}
        for char in exp:
            if char.isalnum(): # if char is alphabet or number we can directly add in res
                res += char
            else:
                if char == '(': # if char is '(' then append it in stack
                    st.append(char)
                elif char == ')': # if char is ')' then pop from stack till and including '('
                    while st[-1] != '(':
                        res += st.pop()
                    st.pop() # to remove '('
                else: # if char is some operator
                    while st and precedence_mapping[char] <= precedence_mapping[st[-1]]: # we need to pop all operator which have higher precedence
                        res += st.pop()
                    st.append(char) # adding the operator after poping all higher precedence operator
        
        while st: # for the remaining operator in stack
            res += st.pop()
        
        return res