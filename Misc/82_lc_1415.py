'''
1415. The k-th Lexicographical String of All Happy Strings of Length n
'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = ''
        l = ['a', 'b', 'c']
        
        ''' base case to handle kth Lexicographical String not existing '''
        d = {1: 3}
        for i in range(2, 11):
            d[i] = 2 * d[i-1]

        if k > d.get(n):
            return res

        def backtrack(path, path_length):
            nonlocal res
            nonlocal k
            if res: return
            if n == path_length:
                k -= 1
                if k == 0:
                    res = "".join(path)
                return
            
            for ind in range(3):
                if (path and path[-1] != l[ind]) or not path:
                    path.append(l[ind])
                    backtrack(path, path_length+1)
                    path.pop()

        backtrack([], 0)
        return res