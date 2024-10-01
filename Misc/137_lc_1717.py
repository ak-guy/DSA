'''
1717. Maximum Score From Removing Substrings
'''

class Solution:
    def getResult(self, s, x, y, givePriorityToX):
        t = 'ab' if givePriorityToX else 'ba'
        st = []
        res = 0
        for char in s:
            if st and st[-1] == t[0] and char == t[1]:
                res += max(x,y)
                st.pop()
                continue
            st.append(char)
        
        toSearch = 'ba' if givePriorityToX else 'ab'
        
        newSt = []
        for char in st:
            if newSt and newSt[-1] == toSearch[0] and char == toSearch[1]:
                res += min(x,y)
                newSt.pop()
                continue
            newSt.append(char)
        
        return res

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            givePriorityToX = True
        else:
            givePriorityToX = False

        return self.getResult(s, x, y, givePriorityToX)